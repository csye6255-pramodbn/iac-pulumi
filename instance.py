import pulumi
from pulumi_aws import ec2
from variables import *
from security_group import *
from myVPC import *
from rds_postgress import *
from iam_policy import *



def generate_user_data(args):
    node_port, db_full_endpoint, db_username, strong_password, db_name, db_dialect = args
    db_host, db_port = db_full_endpoint.split(':')
    return f"""#!/bin/bash
sudo echo PORT="{node_port}" >> /etc/environment
sudo echo DB_HOST="{db_host}" >> /etc/environment
sudo echo DB_PORT="{db_port}" >> /etc/environment
sudo echo DB_USER="{db_username}" >> /etc/environment
sudo echo DB_PASSWORD="{strong_password}" >> /etc/environment
sudo echo DB_NAME="{db_name}" >> /etc/environment
sudo echo DB_DIALECT="{db_dialect}" >> /etc/environment
sudo systemctl daemon-reload
sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a fetch-config -m ec2 -c file:/opt/cloudwatch-config.json -s
sudo systemctl enable amazon-cloudwatch-agent
sudo systemctl start amazon-cloudwatch-agent
sudo systemctl daemon-reload
"""

# Using pulumi.Output.all to combine all outputs into a single tuple.
all_outputs = pulumi.Output.all(node_port, db.endpoint, db_username, strong_password, db_name, db_dialect)

# Using the apply method to generate the user data script with the resolved values.
user_data_script = all_outputs.apply(generate_user_data)

public_ips = []
instance_ids = []
instance_names = []

for i in range(num_instances):
    subnet_id = public_subnets[i % len(public_subnets)].id

    instance = ec2.Instance(f"instance-{i+1}",
                            ami=ami_id,
                            instance_type=instance_type,
                            vpc_security_group_ids=[security_group_id],
                            key_name=keypair_name,
                            subnet_id=subnet_id,
                            associate_public_ip_address=associate_public_ip,
                            root_block_device=ec2.InstanceRootBlockDeviceArgs(
                                volume_size=ebs_size,
                                volume_type=ebs_type,
                                delete_on_termination=delete_on_termination
                            ),
                            disable_api_termination = accidental_termination,
                            user_data=user_data_script,
                            iam_instance_profile=instance_profile.name,
                            tags={
                                "Name": f"{instance_name}-{i+1}",
                            },
                            opts=pulumi.ResourceOptions(depends_on=[db])
                            )
    
    public_ips.append(instance.public_ip)
    instance_ids.append(instance.id)
    instance_names.append(instance.tags["Name"])