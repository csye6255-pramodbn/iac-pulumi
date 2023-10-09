import pulumi
from myVPC import vpc, public_subnets, private_subnets, internet_gateway, public_route_table, private_route_table
from variables import vpc_name, region, profile

# Stack Export
pulumi.export("region", region)
pulumi.export("profile", profile)
pulumi.export("vpc_name", vpc_name)
pulumi.export("vpcId", vpc.id)
pulumi.export("public_subnets_ids", [subnet.id for subnet in public_subnets])
pulumi.export("private_subnets_ids", [subnet.id for subnet in private_subnets])
pulumi.export("public_route_table_id", public_route_table.id)
pulumi.export("private_route_table_id", private_route_table.id)
pulumi.export("internet_gateway_id", internet_gateway.id)