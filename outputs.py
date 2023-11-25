import pulumi
from myVPC import *
from variables import *
from rds_postgress import *
from hosted_zone import *
from cloudwatch_group_stream import *
from load_balancer import *
from auto_scaling_group import *
from sns import *
from aws_lambda import *
from dynamodb import *

# VPC
pulumi.export("region", region)
pulumi.export("profile", profile)
pulumi.export("vpc_name", vpc_name)
pulumi.export("vpcId", vpc.id)

# RDS
pulumi.export("db_id", db.id)
pulumi.export("db_name", db_name)
pulumi.export("db_username", db.username)
pulumi.export("db_port", db.port)
pulumi.export("db_host", db.address)
pulumi.export("db_password", db.password)

# Hosted Zone
pulumi.export("hosted_zone_name", hosted_zone.name)
pulumi.export('demo_record_type', sub_record.type)
pulumi.export('demo_record_name', sub_record.name)

# CloudWatch
pulumi.export('log_group_name', log_group.name)
pulumi.export('log_stream_name', log_stream.name)
pulumi.export('audit_log_group_name', audit_log_group.name)
pulumi.export('audit_log_stream_name', audit_log_stream.name)

# Application Load Balancer
pulumi.export("lb_name", alb.name)
pulumi.export("lb_dns_name", alb_dns_name)
pulumi.export("target_group_name", target_group.name)
pulumi.export("listning_port", listener.port)
pulumi.export("forwarding_port", target_group.port)

# Auto Scaling Group
pulumi.export("launch_template", launch_template.name)
pulumi.export("asg_name", csye6225_asg.name)
pulumi.export("scale_up_policy", scale_up_policy.name)
pulumi.export("scale_down_policy", scale_down_policy.name)
pulumi.export("high_cpu_alarm", high_cpu_alarm.name)
pulumi.export("low_cpu_alarm", low_cpu_alarm.name)

# SNS
pulumi.export("sns_topic_name", sns_topic.name)

# Lambda
pulumi.export("lambda_function_name", lambda_func.name)

# DynamoDB
pulumi.export("dynamodb_table_name", dynamodb_table.name)

