import pulumi
from pulumi_aws import ec2, get_availability_zones
from variables import vpc_cidr, private_subnet_cidr, public_subnet_cidr, vpc_name


avail_zones = get_availability_zones(state="available")

# Creating VPC
vpc = ec2.Vpc(
    "custom_vpc",
    cidr_block=vpc_cidr,
    enable_dns_hostnames=True,
    enable_dns_support=True,
    tags={'Name':vpc_name},
)

# Internet Gateway
internet_gateway = ec2.InternetGateway(
    "internet_gateway",
    vpc_id=vpc.id,
    tags={'Name': 'internet_gateway'}
)

# Public Route Table
public_route_table = ec2.RouteTable(
    "public_route_table",
    vpc_id=vpc.id,
    tags={'Name': 'public_route_table'}
)

# Private Route Table
private_route_table = ec2.RouteTable(
    "private_route_table",
    vpc_id=vpc.id,
    tags={'Name': 'private_route_table'}
)

public_subnets = []
private_subnets = []

# Public Subnets Creation

for i in range(len(public_subnet_cidr)):
    subnet_name = f"public_subnet_{i+1}"
    # Using modulo to cycle through AZs
    az_index = i % len(avail_zones.names)
    public_subnet_cidr[i]
    subnet = ec2.Subnet(
        subnet_name,
        vpc_id=vpc.id,
        cidr_block=public_subnet_cidr[i],
        availability_zone=avail_zones.names[az_index],  # Assign AZ dynamically
        map_public_ip_on_launch=True,  # Setting to True for auto assigning public IP
        tags={'Name': subnet_name}
    )
    public_subnets.append(subnet)

    # Public RouteTable Association
    ec2.RouteTableAssociation(
        f"public_route_table_association_{i+1}",
        route_table_id=public_route_table.id,
        subnet_id=subnet.id
    )

    # Create route for internet gateway  
    ec2.Route(
        f"public_route_{i+1}",
        route_table_id=public_route_table.id,
        destination_cidr_block="0.0.0.0/0",
        gateway_id=internet_gateway.id
    )

for i in range(len(private_subnet_cidr)):
    subnet_name = f"private_subnet_{i+1}"
    # Using modulo to cycle through AZs
    az_index = i % len(avail_zones.names)
    subnet = ec2.Subnet(
        subnet_name,
        vpc_id=vpc.id,
        cidr_block=private_subnet_cidr[i],
        availability_zone=avail_zones.names[az_index],  # Assign AZ dynamically
        tags={'Name': subnet_name}
    )
    private_subnets.append(subnet)

    # Private RouteTable Association
    ec2.RouteTableAssociation(
        f"private_route_table_association_{i+1}",
        route_table_id=private_route_table.id,
        subnet_id=subnet.id
    )