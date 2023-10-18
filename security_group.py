import pulumi
from pulumi_aws import ec2
from variables import security_group_name, sg_ingress_ports
from myVPC import vpc

security_group = ec2.SecurityGroup('security-group',
                          name=security_group_name,
                          description='ssh-http-https-8080',
                          vpc_id=vpc.id,
                          ingress=[
                              ec2.SecurityGroupIngressArgs(
                                  protocol="tcp",
                                  from_port=port,
                                  to_port=port,
                                  cidr_blocks=["0.0.0.0/0"],
                                  ipv6_cidr_blocks=["::/0"]
                              ) for port in sg_ingress_ports
                          ],
                          egress=[
                              ec2.SecurityGroupEgressArgs(
                                  protocol="-1",
                                  from_port=0,
                                  to_port=0,
                                  cidr_blocks=["0.0.0.0/0"],
                                  ipv6_cidr_blocks=["::/0"]
                              )
                          ],
                          tags={
                              "Name": security_group_name
                          })

security_group_id = security_group.id
