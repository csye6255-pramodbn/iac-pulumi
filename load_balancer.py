from pulumi_aws import ec2
import pulumi_aws as aws
from ports import *
from myVPC import *
from variables import *
from myVPC import *


######################################################################################################################################3

# Security Group for Load Balancer

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

# Load Balancer Ingress Rules
lb_ingress_rules = [
    {
        'description': 'HTTP from Anywhere (IPv4)',
        'fromPort': 80,
        'toPort': 80,
        'protocol': 'tcp',
        'cidrBlocks': ['0.0.0.0/0'],
        'ipv6CidrBlocks': ['::/0'],
    },       
    {
        'description': 'HTTPS from Anywhere (IPv4)',
        'fromPort': 443,
        'toPort': 443,
        'protocol': 'tcp',
        'cidrBlocks': ['0.0.0.0/0'],
        'ipv6CidrBlocks': ['::/0'],
    },
]

# Load Balancer Egress Rules
lb_egress_rules = [
    {
        'description': 'All traffic',
        'fromPort': 0,
        'toPort': 0,
        'protocol': '-1',
        'cidrBlocks': ['0.0.0.0/0'],
        'ipv6CidrBlocks': ['::/0'],
    },
]


# Create a Load Balancer Security Group and attach it to the VPC
lb_security_group = ec2.SecurityGroup(
    'loadbalancer-security-group',
    name=loadbalancer_security_group_name,
    description="Application Security Group",
    ingress=transform_rules(lb_ingress_rules),
    egress=transform_rules(lb_egress_rules),
    vpc_id=vpc.id,
    tags={
        "Name": loadbalancer_security_group_name
    }
)
lb_security_group_id = lb_security_group.id


######################################################################################################################################3


# Target Group                                                                                                               
target_group = aws.lb.TargetGroup(tg_name,
    port=tg_port, # 8080
    protocol=tg_protocol, # HTTP
    vpc_id=vpc.id,
    target_type=tg_target_type, # instance
    ip_address_type=tg_ip_address_type, # ipv4
    health_check={ 
        "enabled": tg_enable, # true
        "healthy_threshold": tg_healthy_threshold, # 5
        "interval": tg_interval, # 60
        "path": tg_path, # "/healthz"
        "port": tg_port, # 8080
        "timeout": tg_timeout, # 30   
    },
    tags={"Name": tg_name}
)
target_group_id = target_group.id


# Load Balancer
alb = aws.lb.LoadBalancer(lb_name,
    internal=lb_internal, # false
    security_groups=[lb_security_group_id],
    subnets=public_subnets,
    load_balancer_type=lb_type, # application
    enable_deletion_protection=lb_enable_deletion_protection, # false
    ip_address_type=lb_ip_address_type, # ipv4
    tags={
        "Name": lb_name
    })


# Listener
listener = aws.lb.Listener(lb_listner_name,
    load_balancer_arn=alb.arn,
    port=lb_listener_port, # 80
    protocol=lb_listener_protocol, # HTTP
    default_actions=[{
        "type": lb_listener_default_actions_type, # forward
        "target_group_arn": target_group.arn
    }],
    tags={
        "Name": lb_listner_name
    })

alb_dns_name = alb.dns_name
alb_target_zone_id = alb.zone_id