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



###############################################################################
# Get CLI configs from pulumi config file
cli_region = config1.get('region')
cli_profile = config1.get('profile')
cli_vpc_name = config.get('vpc_name')
cli_vpc_cidr = config.get('vpc_cidr')
cli_public_subnets_cidr = config.get('public_subnets_cidr')
cli_private_subnets_cidr = config.get('private_subnets_cidr')

# Override defaults if CLI config is truthy
if cli_profile:
    profile = cli_profile

if cli_region:
    region = cli_region

if cli_vpc_name:
    vpc_name = cli_vpc_name
    
if cli_vpc_cidr:
    vpc_cidr = cli_vpc_cidr

if cli_public_subnets_cidr:
   public_subnets_cidr = cli_public_subnets_cidr
   
if cli_private_subnets_cidr:
   private_subnets_cidr = cli_private_subnets_cidr