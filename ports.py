import pulumi
from fetch_myip import *

## Application Ingress and Egress Rules
ingress_rules = [
    {
        'description': 'HTTP from Anywhere (IPv4)',
        'fromPort': 80,
        'toPort': 80,
        'protocol': 'tcp',
        'cidrBlocks': ['0.0.0.0/0'],
    },

    {
                'description': 'HTTP from Anywhere (IPv6)',
                'fromPort': 80,
                'toPort': 80,
                'protocol': 'tcp',
                'ipv6CidrBlocks': ['::/0'],
            },
            {
                'description': 'HTTPS from Anywhere (IPv4)',
                'fromPort': 443,
                'toPort': 443,
                'protocol': 'tcp',
                'cidrBlocks': ['0.0.0.0/0'],
            },
            {
                'description': 'HTTPS from Anywhere (IPv6)',
                'fromPort': 443,
                'toPort': 443,
                'protocol': 'tcp',
                'ipv6CidrBlocks': ['::/0'],
            },
            {
                'description': 'SSH from My IP',
                'fromPort': 22,
                'toPort': 22,
                'protocol': 'tcp',
                'cidrBlocks': [my_ip_cidr],
            },
            {
                'description': 'Custom TCP Port 8080 from Anywhere (IPv4)',
                'fromPort': 8080,
                'toPort': 8080,
                'protocol': 'tcp',
                'cidrBlocks': ['0.0.0.0/0'],
            },
            {
                'description': 'Custom TCP Port 8080 from Anywhere (IPv6)',
                'fromPort': 8080,
                'toPort': 8080,
                'protocol': 'tcp',
                'ipv6CidrBlocks': ['::/0'],
            },


]

egress_rules = [
    {
        'protocol': '-1',
        'fromPort': 0,
        'toPort': 0,
        'cidrBlocks': ['0.0.0.0/0'],
        'ipv6CidrBlocks': ['::/0']
    },
]



__all__ = ['ingress_rules', 'egress_rules']