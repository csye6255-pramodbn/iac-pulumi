# Variables
import pulumi
from pulumi import Config
config1 = Config("aws")
config = pulumi.Config()

# defaults
profile = "dev"
region = "default-from-aws-cli"
vpc_name = "My-VPC"
vpc_cidr = "10.0.0.0/16"
public_subnet_cidr = ["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"]
private_subnet_cidr = ["10.0.4.0/24", "10.0.5.0/24", "10.0.6.0/24"]




############################################################################################################

# Get CLI configs from pulumi config file
cli_region = config1.get('region')
cli_profile = config1.get('profile')
cli_vpc_name = config.get('vpc_name')
cli_vpc_cidr = config.get('vpc_cidr')
cli_public_subnets_cidr = config.get('public_subnets_cidr')
cli_private_subnets_cidr = config.get('private_subnets_cidr')


# Remove the brackets and strip unnecessary spaces
clean_string_pub = cli_public_subnets_cidr.strip("[] ")
clean_string_pri = cli_private_subnets_cidr.strip("[] ")

# Split the string into a list based on comma separation
c_pub_cidrs = [block.strip() for block in clean_string_pub.split(",")]
c_pri_cidrs = [block.strip() for block in clean_string_pri.split(",")]


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