import pulumi
from pulumi_aws import ec2
from ports import *
from myVPC import *
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
        transformed.append(transformed_rule)
    return transformed



# Create a security group and attach it to the VPC
security_group = ec2.SecurityGroup(
    'security-group',
    name=security_group_name,
    description="Application Security Group",
    ingress=transform_rules(ingress_rules),
    egress=transform_rules(egress_rules),
    vpc_id=vpc.id,
    tags={
        "Name": security_group_name
    }
)





security_group_id = security_group.id