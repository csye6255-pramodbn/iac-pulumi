import pulumi
from pulumi_aws import ec2, autoscaling, cloudwatch
from variables import *
from application_security_group import *
from myVPC import *
from rds_postgress import *
from iam_policy import *
import base64

#######################################################################################################################
def generate_user_data(args):
  # Input validation
  if not all(args):
    raise Exception("Invalid inputs")

  node_port, db_endpoint, db_username, db_password, db_name, db_dialect = args

  db_host, db_port = db_endpoint.split(':')

  # Full user data script
  user_data = f"""#!/bin/bash
  sudo echo "PORT={node_port}" >> /etc/environment
  sudo echo "DB_HOST={db_host}" >> /etc/environment 
  sudo echo "DB_PORT={db_port}" >> /etc/environment
  sudo echo "DB_USER={db_username}" >> /etc/environment
  sudo echo "DB_PASSWORD={db_password}" >> /etc/environment
  sudo echo "DB_NAME={db_name}" >> /etc/environment  
  sudo echo "DB_DIALECT={db_dialect}" >> /etc/environment
  sudo systemctl daemon-reload
  sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a fetch-config -m ec2 -c file:/opt/cloudwatch-config.json -s
  sudo systemctl enable amazon-cloudwatch-agent
  sudo systemctl start amazon-cloudwatch-agent
  sudo systemctl daemon-reload
  """

  return base64.b64encode(user_data.encode("utf-8")).decode("utf-8")


# Resolve outputs
outputs = pulumi.Output.all(node_port, db.endpoint, db_username, strong_password, db_name, db_dialect) 

# Generate user data 
user_data = outputs.apply(generate_user_data)

# Launch Template
launch_template = ec2.LaunchTemplate(asg_launch_config_name,
    
    name=asg_launch_config_name,
    image_id=ami_id,
    instance_type=asg_ec2_instance_type, # t2.micro
    iam_instance_profile={
        "name": instance_profile.name
    },
    disable_api_termination=asg_accidental_termination, # false
    network_interfaces=[{
        "associate_public_ip_address": asg_associate_public_ip_address, # true
        "security_groups": [application_security_group_id],
    }],
    block_device_mappings=[{
        "device_name": asg_device_name, # /dev/xvda
        "ebs": {
            "delete_on_termination": delete_on_termination, # true
            "volume_size": asg_ebs_volume_size, # 25
            "volume_type": asg_ebs_volume_type, # gp2
        }
    }],
    tag_specifications=[{
        "resource_type": "instance", 
        "tags": {
        "Name": asg_instance_name,
        }
    }],
    key_name=asg_key_name,
    user_data=user_data,
    tags={
        "Name": asg_launch_config_name,
    }       
)

# Auto Scaling Group
csye6225_asg = autoscaling.Group(asg_name,
    desired_capacity=asg_desired_capacity, # 1
    max_size=asg_max_size, # 3
    min_size=asg_min_size, # 1
    default_cooldown=asg_cooldown_period, # 60
    vpc_zone_identifiers=public_subnets,
    launch_template={
                'id': launch_template.id,
                'version': '$Latest',
                },
    target_group_arns=[target_group.arn],
    tags=[
        autoscaling.GroupTagArgs(
            key="asg_key1", # Name
            value=asg_application_name, # my-asg-instance
            propagate_at_launch=asg_propagate_at_launch, # true
        ),
        autoscaling.GroupTagArgs(
            key="asg_key2", # Environment
            value=asg_environment, # Dev/Prod
            propagate_at_launch=asg_propagate_at_launch, # true
        ),
])

###############################################################################################################################################

# ASG Scaling Policy

# Scale Up Policy
scale_up_policy = autoscaling.Policy("scale_up_policy",
    autoscaling_group_name=csye6225_asg.name,
    policy_type=asg_policy_type, # SimpleScaling
    adjustment_type=asg_adjustment_type, # ChangeInCapacity
    scaling_adjustment=asg_scaling_increment, # 1
    cooldown=asg_cooldown_period) # 60

# Scale Down Policy
scale_down_policy = autoscaling.Policy("scale_down_policy",
    autoscaling_group_name=csye6225_asg.name,
    policy_type=asg_policy_type, # SimpleScaling
    adjustment_type=asg_adjustment_type, # ChangeInCapacity
    scaling_adjustment=asg_scaling_decrement, # -1
    cooldown=asg_cooldown_period) # 60

# CloudWatch Metric Alarm - High CPU (Scale Up)
high_cpu_alarm = cloudwatch.MetricAlarm("high_cpu_alarm",
    #alarm_name=asg_high_alaram_name,
    comparison_operator=asg_comparison_operator_up, # GreaterThanThreshold
    evaluation_periods=asg_evaluation_periods, # 1
    metric_name=asg_cpu_metric_name, # CPUUtilization
    namespace=asg_namespace, # AWS/EC2
    period=asg_scaling_period, # 60
    statistic=asg_statistic, # Average
    threshold=asg_cpu_threshold_up, # 5
    dimensions={"AutoScalingGroupName": csye6225_asg.name},
    alarm_actions=[scale_up_policy.arn],
    alarm_description=asg_high_alaram_description)

# CloudWatch Metric Alarm - Low CPU (Scale Down)
low_cpu_alarm = cloudwatch.MetricAlarm("low_cpu_alarm",
    #alarm_name=asg_low_alaram_name,
    comparison_operator=asg_comparison_operator_down, # LessThanThreshold
    evaluation_periods=asg_evaluation_periods, # 1
    metric_name=asg_cpu_metric_name, # CPUUtilization
    namespace=asg_namespace, # AWS/EC2
    period=asg_scaling_period, # 60
    statistic=asg_statistic, # Average
    threshold=asg_cpu_threshold_down, # 3
    dimensions={"AutoScalingGroupName": csye6225_asg.name},
    alarm_actions=[scale_down_policy.arn],
    alarm_description=asg_low_alaram_description)