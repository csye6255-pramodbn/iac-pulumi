import pulumi
from pulumi_aws import ec2
import pulumi_aws as aws
from app_ports import *
from myVPC import *
from load_balancer import *
from variables import *



def transform_rules(rules):
    transformed = []
    for rule in rules:
        transformed_rule = {
            "description": rule.get("description", ""),
            "from_port": rule["fromPort"],
            "to_port": rule["toPort"],
            "protocol": rule["protocol"]
        }
        if "cidrBlocks" in rule:
            transformed_rule["cidr_blocks"] = rule["cidrBlocks"]
        if "ipv6CidrBlocks" in rule:
            transformed_rule["ipv6_cidr_blocks"] = rule["ipv6CidrBlocks"]
        if "securityGroupId" in rule:
            transformed_rule["source_security_group_id"] = rule["securityGroupId"]
        if "security_groups" in rule:
            transformed_rule["security_groups"] = rule["security_groups"]
        transformed.append(transformed_rule)
    return transformed


# Create a EC2 Security Group and attach it to the VPC
application_security_group = ec2.SecurityGroup(
    'security-group',
    name=application_security_group_name,
    description="Application Security Group",
    ingress=transform_rules(app_ingress_rules),
    egress=transform_rules(app_egress_rules),
    vpc_id=vpc.id,
    tags={
        "Name": application_security_group_name
    }
)
application_security_group_id = application_security_group.id


# # Updating the Egress Rule for Load Balancer Security Group
# egress_rule = ec2.SecurityGroupRule('lb_egress_rule',
#     type='egress',
#     from_port=8080,
#     to_port=8080,
#     protocol='tcp',
#     description='Allowing traffic from port 8080 to application security group',
#     source_security_group_id=application_security_group_id,
#     security_group_id=lb_security_group_id
# )