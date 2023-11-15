import pulumi
from fetch_myip import *
from load_balancer import *

# Application Ingress and Egress Rules
app_ingress_rules = [       
    {
        'description': 'SSH from My IP',
        'fromPort': 22,
        'toPort': 22,
        'protocol': 'tcp',
        'cidrBlocks': [my_ip_cidr],
    },
            
    {
        'description': 'Custom TCP Port 8080',
        'fromPort': 8080,
        'toPort': 8080,
        'protocol': 'tcp',
        'security_groups': [lb_security_group_id],
    },
] 

# Application Egress Rule
app_egress_rules = [
    {
        'description': 'All Traffic',
        'fromPort': 0,
        'toPort': 0,
        'protocol': -1,
        'cidrBlocks': ['0.0.0./0'],
        'ipv6CidrBlocks': ['::/0'],
    },
]

__all__ = ['app_ingress_rules', 'app_egress_rules']