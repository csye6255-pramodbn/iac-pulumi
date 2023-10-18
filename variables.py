# Variables
import pulumi
from pulumi import Config
config1 = Config("aws")
config = pulumi.Config()

# VPC Defaults
profile = "dev"
region = "default-from-aws-cli"
vpc_name = "My-VPC"
vpc_cidr = "10.0.0.0/16"
public_subnet_cidr = ["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"]
private_subnet_cidr = ["10.0.4.0/24", "10.0.5.0/24", "10.0.6.0/24"]

# EC2 Instance Default
instance_name = "MyInstance"
ami_id = "ami-06c6f10ccc6bfee60"
num_instances = 1
instance_type = "t2.micro"
ebs_size = 25
ebs_type = "gp2"
delete_on_termination = True
accidental_termination = False
associate_public_ip = True
sg_ingress_ports = [22, 80, 443, 8080]
security_group_name = "application security group"


############################################################################################################

# Get CLI configs from pulumi config file
cli_region = config1.get('region')
cli_profile = config1.get('profile')
cli_vpc_name = config.get('vpc_name')
cli_vpc_cidr = config.get('vpc_cidr')
cli_public_subnets_cidr = config.get('public_subnets_cidr')
cli_private_subnets_cidr = config.get('private_subnets_cidr')

cli_ami_id = config.get('ami_id')
cli_num_instances = config.get_int('num_instances')
cli_instance_type = config.get('instance_type')
cli_ebs_size = config.get_int('ebs_size')
cli_ebs_type = config.get('ebs_type')
cli_delete_on_termination = config.get_bool('delete_on_termination')
cli_accidental_termination = config.get_bool('accidental_termination')
cli_associate_public_ip = config.get_bool('associate_public_ip')
cli_security_group_name = config.get('security_group_name')
cli_sg_ingress_ports = config.get('sg_ingress_ports')


# Remove the brackets and strip unnecessary spaces
clean_string_pub = cli_public_subnets_cidr.strip("[] ")
clean_string_pri = cli_private_subnets_cidr.strip("[] ")
clean_string_ports = cli_sg_ingress_ports.strip("[] ")

# Split the string into a list based on comma separation
c_pub_cidrs = [block.strip() for block in clean_string_pub.split(",")]
c_pri_cidrs = [block.strip() for block in clean_string_pri.split(",")]
c_sg_ingress_ports = [port.strip() for port in clean_string_ports.split(",")]


# Override defaults if CLI config is truthy
if cli_profile:
    profile = cli_profile

if cli_region:
    region = cli_region

if cli_vpc_name:
    vpc_name = cli_vpc_name
    
if cli_vpc_cidr:
    vpc_cidr = cli_vpc_cidr

if c_pub_cidrs:
   public_subnet_cidr = c_pub_cidrs

if c_pri_cidrs:
   private_subnet_cidr = c_pri_cidrs


if cli_ami_id:
    ami_id = cli_ami_id

if cli_num_instances:
    num_instances = cli_num_instances

if cli_instance_type:
    instance_type = cli_instance_type

if cli_ebs_size:
    ebs_size = cli_ebs_size

if cli_ebs_type:
    ebs_type = cli_ebs_type

if cli_delete_on_termination:
    delete_on_termination = cli_delete_on_termination

if cli_accidental_termination:
    accidental_termination = cli_accidental_termination

if cli_associate_public_ip:
    associate_public_ip = cli_associate_public_ip

if cli_security_group_name:
    security_group_name = cli_security_group_name

if c_sg_ingress_ports:
    sg_ingress_ports = c_sg_ingress_ports