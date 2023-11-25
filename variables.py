# Variables
import pulumi
from pulumi import Config
config1 = Config("aws")
config = pulumi.Config()

############################################################################################################

# You can just use the default values below or override them with CLI configs

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
application_security_group_name = "application security group"

# RDS Instance Default
db_security_group_name = "database security group"
db_engine = "postgres"
db_engine_version = "14.6"
db_instance_class = "db.t3.micro"
db_identifier = "csye6225"
db_multi_az = False
db_username = "csye6225"
db_name = "csye6225"
db_password = "Pramod123Pramod123Pramod123"
db_publicly_accessible = False
db_allocated_storage = 10
db_max_allocated_storage = 50
db_skip_final_snapshot = True

# Parameter Group for RDS Defaults
db_parameter_group_name = "csye6225"
db_parameter_group_family = "postgres14"
db_parameter_group_description = "Parameter Group for CSYE 6225"
db_parameter_group_max_connections = 100

# For EC2 User Data
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
audit_log_group_name = "audit-group"
audit_log_stream_name = "audit-stream"
lambda_log_group_name = "lambda-group"
lambda_log_stream_name = "lambda-stream"

# Target Group Defaults
tg_name = "MyTargetGroup"
tg_port = 8080
tg_protocol = "HTTP" 
tg_target_type = "instance"
tg_ip_address_type = "ipv4"
tg_enable = True
tg_path = "/healthz"
tg_healthy_threshold = 5
tg_timeout = 30
tg_interval = 60

# Load Balancer SG Defaults
loadbalancer_security_group_name = "loadbalancer-security-group"

# Load Balancer Defaults
lb_name = "MyALB"
lb_load_balancer_type = "application"
lb_enable_deletion_protection = False
lb_internal = False #Internet facing
lb_ip_address_type = "ipv4"
alb_evaluate_target_health = True

# Load Balancer Listener Defaults
lb_listner_name = "MyListener"
lb_type = "application"
lb_listener_port = 80
lb_listener_protocol = "HTTP"
lb_listener_default_actions_type = "forward"

# Launch Template Defaults
asg_launch_config_name = "asg_launch_config"
asg_ec2_instance_type = "t2.micro"
asg_key_name = "mykey"
asg_device_name = "/dev/xvda"
asg_ebs_volume_size = 25
asg_ebs_volume_type = "gp2"
asg_delete_on_termination = True
asg_accidental_termination = False
asg_associate_public_ip_address = True

# Auto Scaling Group Defaults
asg_name = "MyASG"
asg_min_size = 1
asg_max_size = 3
asg_desired_capacity = 1
asg_cooldown_period = 60
asg_key1 = "Name"
asg_application_name = "csye6225_webapp"
asg_key2 = "Environment"
asg_environment = "demo/prod"
asg_propagate_at_launch = True
asg_instance_name = "my-asg-instance"

# Auto Scaling Group Policy Defaults
asg_scaling_increment = 1
asg_scaling_decrement = -1
asg_scaling_period = 60
asg_evaluation_periods = 1
asg_high_alaram_name = "high_cpu"
asg_low_alaram_name = "low_cpu"
asg_high_alaram_description = "Scale up if CPU > 5% for 1 minute"
asg_low_alaram_description = "Scale down if CPU < 3% for 1 minute"
asg_policy_type = "SimpleScaling"
asg_adjustment_type = "ChangeInCapacity"
asg_statistic = "Average"
asg_cpu_metric_name = "CPUUtilization"
asg_comparison_operator_up = "GreaterThanThreshold"
asg_comparison_operator_down = "LessThanThreshold"
asg_cpu_threshold_up = 5
asg_cpu_threshold_down = 3
asg_namespace = "AWS/EC2"

# Lambda Defaults
lambda_name = "mylambda"

# SNS Defaults
sns_topic_name = "myTopic"
sns_subscription_name = "mySubscription"

# GCP Defaults
gcp_bucket_name = "mybucket"
gcp_bucket_location = "US"
bucket_force_destroy = True
project_id = "dev-gcp-405522"
gcp_service_account_name = "my-service-account"
gcp_service_display_account_name = "My-Storage-Admin-Service-Account"

# DynamoDB Defaults
dynamodb_table_name = "myDynamo"

############################################################################################################

# Get CLI configs from pulumi config file

# VPC Defaults
cli_region = config1.get('region')
cli_profile = config1.get('profile')
cli_vpc_name = config.get('vpc_name')
cli_vpc_cidr = config.get('vpc_cidr')
cli_public_subnets_cidr = config.get('public_subnets_cidr')
cli_private_subnets_cidr = config.get('private_subnets_cidr')

# EC2 Instance Default
cli_instance_name = config.get('instance_name')
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

# RDS Instance Default
cli_db_security_group_name = config.get('db_security_group_name')
cli_db_engine = config.get('db_engine')
cli_db_engine_version = config.get('db_engine_version')
cli_db_instance_class = config.get('db_instance_class')
cli_db_identifier = config.get('db_identifier')
cli_db_multi_az = config.get_bool('db_multi_az')
cli_db_username = config.get('db_username')
cli_db_name = config.get('db_name')
cli_db_password = config.get('db_password')
cli_db_publicly_accessible = config.get_bool('db_publicly_accessible')
cli_db_allocated_storage = config.get_int('db_allocated_storage')
cli_db_max_allocated_storage = config.get_int('db_max_allocated_storage')
cli_db_skip_final_snapshot = config.get_bool('db_skip_final_snapshot')

# Parameter Group for RDS Defaults
cli_db_parameter_group_name = config.get('db_parameter_group_name')
cli_db_parameter_group_family = config.get('db_parameter_group_family')
cli_db_parameter_group_description = config.get('db_parameter_group_description')
cli_db_parameter_group_max_connections = config.get_int('db_parameter_group_max_connections')

# For EC2 User Data
cli_db_port = config.get_int('db_port')
cli_node_port = config.get_int('node_port')
cli_db_dialect = config.get('db_dialect')

# Route53 Defaults
cli_zone_name = config.get('zone_name')
cli_ttl = config.get_int('ttl')
cli_A_record = config.get('A_record')

# CloudWatch Defaults
cli_cloudwatch_log_group_name = config.get('log_group_name')
cli_cloudwatch_log_stream_name = config.get('log_stream_name')
cli_audit_log_group_name = config.get('audit_log_group_name')
cli_audit_log_stream_name = config.get('audit_log_stream_name')

# Target Group Defaults
cli_tg_name = config.get('tg_name')
cli_tg_port = config.get('tg_port')
cli_tg_protocol = config.get('tg_protocol')
cli_tg_target_type = config.get('tg_target_type')
cli_tg_ip_address_type = config.get('tg_ip_address_type')
cli_tg_enable = config.get('tg_enable')
cli_tg_path = config.get('tg_path')
cli_tg_healthy_threshold = config.get('tg_healthy_threshold')
cli_tg_timeout = config.get('tg_timeout')
cli_tg_interval = config.get('tg_interval')

# Load Balancer SG Defaults
cli_loadbalancer_security_group_name = config.get('loadbalancer_security_group_name')

# Load Balancer Defaults
cli_lb_name = config.get('lb_name')
cli_lb_load_balancer_type = config.get('lb_load_balancer_type')
cli_lb_enable_deletion_protection = config.get('lb_enable_deletion_protection')
cli_lb_internal = config.get('lb_internal') #Internet facing
cli_lb_ip_address_type = config.get('lb_ip_address_type')
cli_alb_evaluate_target_health = config.get('alb_evaluate_target_health')

# Load Balancer Listener Defaults
cli_lb_listner_name = config.get('lb_listner_name')
cli_lb_type = config.get('lb_type')
cli_lb_listener_port = config.get('lb_listener_port')
cli_lb_listener_protocol = config.get('lb_listener_protocol')
cli_lb_listener_default_actions_type = config.get('lb_listener_default_actions_type')

# Launch Template Defaults
cli_asg_launch_config_name = config.get('asg_launch_config_name')
cli_asg_ec2_instance_type = config.get('asg_ec2_instance_type')
cli_asg_key_name = config.get('asg_key_name')
cli_asg_device_name = config.get('asg_device_name')
cli_asg_ebs_volume_size = config.get('asg_ebs_volume_size')
cli_asg_ebs_volume_type = config.get('asg_ebs_volume_type')
cli_asg_delete_on_termination = config.get('asg_delete_on_termination')
cli_asg_accidental_termination = config.get('asg_accidental_termination')
cli_asg_associate_public_ip_address = config.get('asg_associate_public_ip_address')

# Auto Scaling Group Defaults
cli_asg_name = config.get('asg_name')
cli_asg_min_size = config.get('asg_min_size')
cli_asg_max_size = config.get('asg_max_size')
cli_asg_desired_capacity = config.get('asg_desired_capacity')
cli_asg_cooldown_period = config.get('asg_cooldown_period')
cli_asg_key1 = config.get('asg_key1')
cli_asg_application_name = config.get('asg_application_name')
cli_asg_key2 = config.get('asg_key2')
cli_asg_environment = config.get('asg_environment')
cli_asg_propagate_at_launch = config.get('asg_propagate_at_launch')
cli_asg_instance_name = config.get('asg_instance_name')

# Auto Scaling Group Policy Defaults
cli_asg_scaling_increment = config.get('asg_scaling_increment')
cli_asg_scaling_decrement = config.get('asg_scaling_decrement')
cli_asg_scaling_period = config.get('asg_scaling_period')
cli_asg_evaluation_periods = config.get('asg_evaluation_periods')
cli_asg_high_alaram_name = config.get('asg_high_alaram_name')
cli_asg_low_alaram_name = config.get('asg_low_alaram_name')
cli_asg_high_alaram_description = config.get('asg_high_alaram_description')
cli_asg_low_alaram_description = config.get('asg_low_alaram_description')
cli_asg_policy_type = config.get('asg_policy_type')
cli_asg_adjustment_type = config.get('asg_adjustment_type')
cli_asg_statistic = config.get('asg_statistic')
cli_asg_cpu_metric_name = config.get('asg_cpu_metric_name')
cli_asg_comparison_operator_up = config.get('asg_comparison_operator_up')
cli_asg_comparison_operator_down = config.get('asg_comparison_operator_down')
cli_asg_cpu_threshold_up = config.get('asg_cpu_threshold_up')
cli_asg_cpu_threshold_down = config.get('asg_cpu_threshold_down')
cli_asg_namespace = config.get('asg_namespace')

# Lambda Defaults
cli_lambda_name = config.get('lambda_name')

# SNS Defaults
cli_sns_topic_name = config.get('sns_topic_name')
cli_sns_subscription_name = config.get('sns_subscription_name')

# GCP Defaults
cli_project_id = config.get("gcp:project")
cli_gcp_bucket_name = config.get("gcp_bucket_name")
cli_gcp_bucket_location = config.get("gcp_bucket_location")
cli_bucket_force_destroy = config.get_bool("bucket_force_destroy")
cli_gcp_service_account_name = config.get("gcp_service_account_name")
cli_gcp_service_display_account_name = config.get("gcp_service_display_account_name")

# DynamoDB Defaults
cli_dynamodb_table_name = config.get("dynamodb_table_name")


############################################################################################################

# Regular Expressions

# Remove the brackets and strip unnecessary spaces
clean_string_pub = cli_public_subnets_cidr.strip("[] ")
clean_string_pri = cli_private_subnets_cidr.strip("[] ")

# Split the string into a list based on comma separation
c_pub_cidrs = [block.strip() for block in clean_string_pub.split(",")]
c_pri_cidrs = [block.strip() for block in clean_string_pri.split(",")]


############################################################################################################

# Override defaults if CLI config is truthy

# VPC Defaults
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


# EC2 Instance Default
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


# RDS Instance Default
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
if cli_db_password:
    db_password = cli_db_password
if cli_db_publicly_accessible:
    db_publicly_accessible = cli_db_publicly_accessible
if cli_db_allocated_storage:
    db_allocated_storage = cli_db_allocated_storage
if cli_db_max_allocated_storage:
    db_max_allocated_storage = cli_db_max_allocated_storage
if cli_db_skip_final_snapshot:
    db_skip_final_snapshot = cli_db_skip_final_snapshot

# Parameter Group for RDS Defaults
if cli_db_parameter_group_name:
    db_parameter_group_name = cli_db_parameter_group_name
if cli_db_parameter_group_family:
    db_parameter_group_family = cli_db_parameter_group_family
if cli_db_parameter_group_description:
    db_parameter_group_description = cli_db_parameter_group_description
if cli_db_parameter_group_max_connections:
    db_parameter_group_max_connections = cli_db_parameter_group_max_connections

# For EC2 User Data
if cli_db_port:
    db_port = cli_db_port
if cli_node_port:
    node_port = cli_node_port
if cli_db_dialect:
    db_dialect = cli_db_dialect


# Route53 Defaults
if cli_zone_name:
    zone_name = cli_zone_name
if cli_ttl:
    ttl = cli_ttl
if cli_A_record:
    A_record = cli_A_record


# CloudWatch Defaults
if cli_cloudwatch_log_group_name:
    log_group_name = cli_cloudwatch_log_group_name
if cli_cloudwatch_log_stream_name:
    log_stream_name = cli_cloudwatch_log_stream_name
if cli_audit_log_group_name:
    audit_log_group_name = cli_audit_log_group_name
if cli_audit_log_stream_name:
    audit_log_stream_name = cli_audit_log_stream_name


# Target Group Defaults
if cli_tg_name:
    tg_name = cli_tg_name
if cli_tg_port:
    tg_port = cli_tg_port
if cli_tg_protocol:
    tg_protocol = cli_tg_protocol
if cli_tg_target_type:
    tg_target_type = cli_tg_target_type
if cli_tg_ip_address_type:
    tg_ip_address_type = cli_tg_ip_address_type
if cli_tg_enable:
    tg_enable = cli_tg_enable
if cli_tg_path:
    tg_path = cli_tg_path
if cli_tg_healthy_threshold:
    tg_healthy_threshold = cli_tg_healthy_threshold
if cli_tg_timeout:
    tg_timeout = cli_tg_timeout
if cli_tg_interval:
    tg_interval = cli_tg_interval

# Load Balancer SG Defaults
if cli_loadbalancer_security_group_name:
    loadbalancer_security_group_name = cli_loadbalancer_security_group_name

# Load Balancer Defaults
if cli_lb_name:
    lb_name = cli_lb_name
if cli_lb_load_balancer_type:
    lb_load_balancer_type = cli_lb_load_balancer_type
if cli_lb_enable_deletion_protection:
    lb_enable_deletion_protection = cli_lb_enable_deletion_protection
if cli_lb_internal:
    lb_internal = cli_lb_internal
if cli_lb_ip_address_type:
    lb_ip_address_type = cli_lb_ip_address_type
if cli_alb_evaluate_target_health:
    alb_evaluate_target_health = cli_alb_evaluate_target_health

# Load Balancer Listener Defaults
if cli_lb_listner_name:
    lb_listner_name = cli_lb_listner_name
if cli_lb_type:
    lb_type = cli_lb_type
if cli_lb_listener_port:
    lb_listener_port = cli_lb_listener_port
if cli_lb_listener_protocol:
    lb_listener_protocol = cli_lb_listener_protocol
if cli_lb_listener_default_actions_type:
    lb_listener_default_actions_type = cli_lb_listener_default_actions_type

# Launch Template Defaults
if cli_asg_launch_config_name:
    asg_launch_config_name = cli_asg_launch_config_name
if cli_asg_ec2_instance_type:
    asg_ec2_instance_type = cli_asg_ec2_instance_type
if cli_asg_key_name:
    asg_key_name = cli_asg_key_name
if cli_asg_device_name:
    asg_device_name = cli_asg_device_name
if cli_asg_ebs_volume_size:
    asg_ebs_volume_size = cli_asg_ebs_volume_size
if cli_asg_ebs_volume_type:
    asg_ebs_volume_type = cli_asg_ebs_volume_type
if cli_asg_delete_on_termination:
    asg_delete_on_termination = cli_asg_delete_on_termination
if cli_asg_accidental_termination:
    asg_accidental_termination = cli_asg_accidental_termination
if cli_asg_associate_public_ip_address:
    asg_associate_public_ip_address = cli_asg_associate_public_ip_address

# Auto Scaling Group Defaults
if cli_asg_name:
    asg_name = cli_asg_name
if cli_asg_min_size:
    asg_min_size = cli_asg_min_size
if cli_asg_max_size:
    asg_max_size = cli_asg_max_size
if cli_asg_desired_capacity:
    asg_desired_capacity = cli_asg_desired_capacity
if cli_asg_cooldown_period:
    asg_cooldown_period = cli_asg_cooldown_period
if cli_asg_key1:
    asg_key1 = cli_asg_key1
if cli_asg_application_name:
    asg_application_name = cli_asg_application_name
if cli_asg_key2:
    asg_key2 = cli_asg_key2
if cli_asg_environment:
    asg_environment = cli_asg_environment
if cli_asg_propagate_at_launch:
    asg_propagate_at_launch = cli_asg_propagate_at_launch
if cli_asg_instance_name:
    asg_instance_name = cli_asg_instance_name

# Auto Scaling Group Policy Defaults
if cli_asg_scaling_increment:
    asg_scaling_increment = cli_asg_scaling_increment
if cli_asg_scaling_decrement:
    asg_scaling_decrement = cli_asg_scaling_decrement
if cli_asg_scaling_period:
    asg_scaling_period = cli_asg_scaling_period
if cli_asg_evaluation_periods:
    asg_evaluation_periods = cli_asg_evaluation_periods
if cli_asg_high_alaram_name:
    asg_high_alaram_name = cli_asg_high_alaram_name
if cli_asg_low_alaram_name:
    asg_low_alaram_name = cli_asg_low_alaram_name
if cli_asg_high_alaram_description:
    asg_high_alaram_description = cli_asg_high_alaram_description
if cli_asg_low_alaram_description:
    asg_low_alaram_description = cli_asg_low_alaram_description
if cli_asg_policy_type:
    asg_policy_type = cli_asg_policy_type
if cli_asg_adjustment_type:
    asg_adjustment_type = cli_asg_adjustment_type
if cli_asg_statistic:
    asg_statistic = cli_asg_statistic
if cli_asg_cpu_metric_name:
    asg_cpu_metric_name = cli_asg_cpu_metric_name
if cli_asg_comparison_operator_up:
    asg_comparison_operator_up = cli_asg_comparison_operator_up
if cli_asg_comparison_operator_down:
    asg_comparison_operator_down = cli_asg_comparison_operator_down
if cli_asg_cpu_threshold_up:
    asg_cpu_threshold_up = cli_asg_cpu_threshold_up
if cli_asg_cpu_threshold_down:
    asg_cpu_threshold_down = cli_asg_cpu_threshold_down
if cli_asg_namespace:
    asg_namespace = cli_asg_namespace

# Lambda Defaults
if cli_lambda_name:
    lambda_name = cli_lambda_name

# SNS Defaults
if cli_sns_topic_name:
    sns_topic_name = cli_sns_topic_name
if cli_sns_subscription_name:
    sns_subscription_name = cli_sns_subscription_name

# GCP Defaults
if cli_project_id:
    project_id = cli_project_id
if cli_gcp_bucket_name:
    gcp_bucket_name = cli_gcp_bucket_name
if cli_gcp_bucket_location:
    gcp_bucket_location = cli_gcp_bucket_location
if cli_bucket_force_destroy:
    bucket_force_destroy = cli_bucket_force_destroy
if cli_gcp_service_account_name:
    gcp_service_account_name = cli_gcp_service_account_name
if cli_gcp_service_display_account_name:
    gcp_service_display_account_name = cli_gcp_service_display_account_name