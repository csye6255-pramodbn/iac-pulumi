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
ami_id = "ami-0e58206c8b17a9a3c"
keypair_name = "mykey"
num_instances = 1
instance_type = "t2.micro"
ebs_size = 25
ebs_type = "gp2"
delete_on_termination = True
accidental_termination = False
associate_public_ip = True
security_group_name = "application security group"


# RDS Instance Default
db_security_group_name = "database security group"
db_engine = "postgres"
db_engine_version = "14.6"
db_instance_class = "db.t3.micro"
db_identifier = "csye6225"
db_multi_az = False
db_username = "csye6225"
db_name = "csye6225"
db_publicly_accessible = False
db_allocated_storage = 10
db_max_allocated_storage = 50
db_skip_final_snapshot = True

db_parameter_group_name = "csye6225"
db_parameter_group_family = "postgres14"
db_parameter_group_description = "Parameter Group for CSYE 6225"
db_parameter_group_max_connections = 100

db_port = 5432
node_port = 8080
db_dialect = "postgres"


# Route53 Defaults
zone_name = 'demo.pramod.cloud'
ttl = 300
A_record = 'A'

# CloudWatch Defaults
log_group_name = "csye6225"
log_stream_name = "webapp"

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
cli_keypair_name = config.get('keypair_name')
cli_instance_name = config.get('instance_name')

cli_db_security_group_name = config.get('db_security_group_name')
cli_db_engine = config.get('db_engine')
cli_db_engine_version = config.get('db_engine_version')
cli_db_instance_class = config.get('db_instance_class')
cli_db_identifier = config.get('db_identifier')
cli_db_multi_az = config.get_bool('db_multi_az')
cli_db_username = config.get('db_username')
cli_db_name = config.get('db_name')
cli_db_publicly_accessible = config.get_bool('db_publicly_accessible')
cli_db_allocated_storage = config.get_int('db_allocated_storage')
cli_db_max_allocated_storage = config.get_int('db_max_allocated_storage')
cli_db_skip_final_snapshot = config.get_bool('db_skip_final_snapshot')

cli_db_parameter_group_name = config.get('db_parameter_group_name')
cli_db_parameter_group_family = config.get('db_parameter_group_family')
cli_db_parameter_group_description = config.get('db_parameter_group_description')
cli_db_parameter_group_max_connections = config.get_int('db_parameter_group_max_connections')

cli_db_port = config.get_int('db_port')
cli_node_port = config.get_int('node_port')
cli_db_dialect = config.get('db_dialect')

cli_zone_name = config.get('zone_name')

cli_cloudwatch_log_group_name = config.get('log_group_name')
cli_cloudwatch_log_stream_name = config.get('log_stream_name')

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

if cli_keypair_name:
    keypair_name = cli_keypair_name

if cli_instance_name:
    instance_name = cli_instance_name

if cli_db_security_group_name:
    db_security_group_name = cli_db_security_group_name

if cli_db_engine:
    db_engine = cli_db_engine

if cli_db_engine_version:
    db_engine_version = cli_db_engine_version

if cli_db_instance_class:
    db_instance_class = cli_db_instance_class

if cli_db_identifier:
    db_identifier = cli_db_identifier

if cli_db_multi_az:
    db_multi_az = cli_db_multi_az

if cli_db_username:
    db_username = cli_db_username

if cli_db_name:
    db_name = cli_db_name

if cli_db_publicly_accessible:
    db_publicly_accessible = cli_db_publicly_accessible

if cli_db_allocated_storage:
    db_allocated_storage = cli_db_allocated_storage

if cli_db_max_allocated_storage:
    db_max_allocated_storage = cli_db_max_allocated_storage

if cli_db_skip_final_snapshot:
    db_skip_final_snapshot = cli_db_skip_final_snapshot



if cli_db_parameter_group_name:
    db_parameter_group_name = cli_db_parameter_group_name

if cli_db_parameter_group_family:
    db_parameter_group_family = cli_db_parameter_group_family

if cli_db_parameter_group_description:
    db_parameter_group_description = cli_db_parameter_group_description

if cli_db_parameter_group_max_connections:
    db_parameter_group_max_connections = cli_db_parameter_group_max_connections



if cli_db_port:
    db_port = cli_db_port

if cli_node_port:
    node_port = cli_node_port

if cli_db_dialect:
    db_dialect = cli_db_dialect


if cli_zone_name:
    zone_name = cli_zone_name


if cli_cloudwatch_log_group_name:
    log_group_name = cli_cloudwatch_log_group_name

if cli_cloudwatch_log_stream_name:
    log_stream_name = cli_cloudwatch_log_stream_name