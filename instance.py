import pulumi
from pulumi_aws import ec2
from myVPC import public_subnets
from variables import num_instances, instance_type, ebs_size, ebs_type, delete_on_termination, accidental_termination, ami_id, associate_public_ip, instance_name
from security_group import security_group_id
from keypair import key_pair


for i in range(0, num_instances):
  subnet_id = public_subnets[i % len(public_subnets)].id
  instance = ec2.Instance(f"instance-{i+1}",
    key_name=key_pair.key_name,
    subnet_id=subnet_id,
    ami=ami_id,
    instance_type = instance_type,
    vpc_security_group_ids = [security_group_id],
    associate_public_ip_address = associate_public_ip, 
    root_block_device={
        "volume_size": ebs_size,
        "volume_type": ebs_type,
        "delete_on_termination": delete_on_termination
    },
    disable_api_termination = accidental_termination,
    
    tags={
    "Name": instance_name 
  }
   
  )