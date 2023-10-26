import pulumi
import secrets
import pulumi_aws as aws
from pulumi_aws import ec2, rds
from myVPC import *
from variables import *
from security_group import *





## Database Ingress and Egress Rules
db_ingress_rules = [
    {
        'description': 'HTTP from Anywhere (IPv4)',
        'fromPort': 5432,
        'toPort': 5432,
        'protocol': 'tcp',
        #'cidrBlocks': ['0.0.0.0/0'],
        'security_groups': [security_group_id]
    },
]

# db_egress_rules = [
#     {
#         'protocol': '-1',
#         'fromPort': 0,
#         'toPort': 0,
#         'cidrBlocks': ['0.0.0.0/0'],
#         'ipv6CidrBlocks': ['::/0']
#     },
# ]

# Database Security Group
db_security_group = ec2.SecurityGroup(
    'db-security-group',
    name=db_security_group_name,
    description="Database Security Group",
    ingress= db_ingress_rules,
    #egress= db_egress_rules,
    vpc_id=vpc.id,

    tags={
        "Name": db_security_group_name
    }
)

# Parameter Group for RDS
postgres_param_group = aws.rds.ParameterGroup(
    db_parameter_group_name,
    name=db_parameter_group_name,
    family=db_parameter_group_family,
    description=db_parameter_group_description,
    parameters=[
        {
            "name": "max_connections",
            "value": "100",
            "apply_method": "pending-reboot"
        }
    ]
)


# Private Subnets for RDS
db_subnet_group = rds.SubnetGroup("db-subnet-group",
    subnet_ids=private_subnets,
    tags={
        "Name": "db-subnet-group"
    }
)

# Random Password Generator
strong_password = secrets.token_urlsafe(16)

# Creating RDS
db = rds.Instance('postgres',
    engine = db_engine,
    engine_version = db_engine_version,
    instance_class = db_instance_class,
    identifier = db_identifier,
    multi_az = db_multi_az,
    username = db_username,
    password = strong_password,
    parameter_group_name = postgres_param_group,
    db_name = db_name,
    db_subnet_group_name = db_subnet_group, 
    publicly_accessible = db_publicly_accessible,
    vpc_security_group_ids = [db_security_group.id],
    allocated_storage = db_allocated_storage,
    max_allocated_storage = db_max_allocated_storage,
    skip_final_snapshot = db_skip_final_snapshot,

    tags={
        "Name": db_identifier
    }

    )

db_id = db.id
db_endpoint = db.endpoint