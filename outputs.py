import pulumi
from myVPC import *
from variables import *
from security_group import *
from instance import *
from rds_postgress import *
from hosted_zone import *
from cloudwatch_group_stream import *

# VPC
pulumi.export("region", region)
pulumi.export("profile", profile)
pulumi.export("vpc_name", vpc_name)
pulumi.export("vpcId", vpc.id)
pulumi.export("public_subnets_ids", [subnet.id for subnet in public_subnets])
pulumi.export("private_subnets_ids", [subnet.id for subnet in private_subnets])
pulumi.export("public_route_table_id", public_route_table.id)
pulumi.export("private_route_table_id", private_route_table.id)
pulumi.export("internet_gateway_id", internet_gateway.id)

# EC2 & Security Group
pulumi.export("ami_id", ami_id)
pulumi.export("num_instances", num_instances)
pulumi.export('instance_names', pulumi.Output.all(*instance_names))
pulumi.export('public_ips', pulumi.Output.all(*public_ips))
pulumi.export('instance_ids', pulumi.Output.all(*instance_ids))
pulumi.export('security_group_id', security_group.id)
pulumi.export("group_name",  security_group.name)

# RDS
pulumi.export("db_id", db.id)
pulumi.export("db_name", db_name)
pulumi.export("db_username", db.username)
pulumi.export("db_port", db.port)
pulumi.export("db_host", db.address)
pulumi.export("db_password", db.password)

# Hosted Zone
pulumi.export("hosted_zone_name", hosted_zone.name)
pulumi.export('demo_record_type', demo_record.type)
pulumi.export('demo_record_name', demo_record.name)
pulumi.export('www_record_type', www_record.type)
pulumi.export('www_record_name', www_record.name)

# CloudWatch
pulumi.export('log_group_name', log_group.name)
pulumi.export('log_stream_name', log_stream.name)