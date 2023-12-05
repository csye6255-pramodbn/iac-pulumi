## Name: Pramod Begur Nagaraj
## NUID: 002708842 

# Pulumi IaC

## AWS Networking Setup
The code does the following:
1. Creates a new Virtual Private Cloud (VPC)
2. Creates 6 subnets in the new VPC.  3 public subnets and 3 private subnets, each in a different availability zone in the same region as the VPC
3. Creates an Internet Gateway Links and attaches the Internet Gateway to the VPC
4. Creates a public route table and attaches all public subnets created to the route table
5. Creates a private route table and attaches all private subnets created to the route table
6. Creates a public route in the public route table created above with the destination CIDR block 0.0.0.0/0 and the internet gateway created above as the target

## Application Security Group

### SSH:
- **Port: 22**
- **Source: Only from my IP**

### Application Port:
- **Port: 8080**
-  **Source: ALB security group**

### Outbound:
- **Allowing traffic from port 5432 to database security group**


## IAM Roles

### AmazonRDSFullAccess
- Description: Provides full access to Amazon RDS resources.
- Permissions: arn:aws:iam::aws:policy/AmazonRDSFullAccess

### CloudWatchAgentServerPolicy
- Description: Grants permissions for the CloudWatch agent on server instances.
- Permissions: arn:aws:iam::aws:policy/CloudWatchAgentServerPolicy"

### SNSFullAccessPolicy
- Description: Grants permission to publish messages to SNS Topic
- Permission: arn:aws:iam::aws:policy/AmazonSNSFullAccess

## EC2 Instance Configuration

- **AMI**: Uses a custom Amazon Machine Image (AMI), generated by Packer.
- **Protection**: The instance does **not** have protection against accidental termination.
- **Root Volume**: 
  - **Size**: 25 GB.
  - **Type**: General Purpose SSD (GP2).
- **Security Group**: The previously described security group is attached to this EC2 instance.
- **EBS Termination**: EBS volumes will be terminated concurrently with the EC2 instance termination.
- **Userdata**: DB Configs to store in /etc/environment.

## PostgreSQL RDS Setup on AWS

### 📌 RDS Instance
- **Name:** `csye6225`
- **Engine:** PostgreSQL

### 🌐 Subnet Group
- Created using all the private subnets from the custom VPC.

### 🔧 Parameter Group
- **Parameter:** 
  - `Max Connections`: 100

### 🔒 Security Group
- **Inbound Rule:**
  - **Port:** `5432`
  - **Source:** Application security group

# Load Balancer Configuration

This README outlines the configuration for our load balancer setup, including details on the Application Load Balancer (ALB), Target Group, Listener, Auto Scaling Group (ASG), ASG Policies, and DNS Record.

## Application Load Balancer (ALB)

- **Type:** Internet Facing
- **Security Group Settings:**
  - **Ingress:** Ports 443
  - **Egress:** Allowing traffic from port 8080 to application security group

## Target Group

- **Targets:** Port 8080
- **Health Checks:** Checks applications at `/healthz`

## Listener

- **Listens:** On port 443
- **Forwards:** To port 8080

## Auto Scaling Group (ASG)

- **Desired Capacity:** 1
- **Minimum Capacity:** 1
- **Maximum Capacity:** 3

## ASG Policy

- **Scale Up:** When average CPU usage is above 5%. Increment by 1.
- **Scale Down:** When average CPU usage is below 3%. Decrement by 1.

## DNS Record

- **Type:** A record
- **Points to:** ALB `dns_name`


## CloudWatch

### Log Groups

#### csye6225
- Description: Log group for the web application.
- Log Streams: 
  - webapp
    - Description: Log stream for the web application.

#### audit-group
- Description: Log group for auditing purposes.
- Log Streams:
  - audit-stream
    - Description: Log stream for auditing events.



## Google Cloud Platform (GCP) Setup

### Bucket Creation
- A bucket has been created in GCP for storage purposes.

### Service Account
- A Service Account has been created.
- The `Storage Admin` role is attached to this Service Account for necessary permissions.
- An access key has been generated for this Service Account.

## AWS Setup

### DynamoDB
- A DynamoDB table has been created for database needs.

### Lambda Function
- A Lambda function has been established.
- Lambda Code is passed as zip file through pulumi
- Environment Variables:
  - GCP private access key
  - GCP bucket name
  - DynamoDB table name
- IAM Role and Permissions:
  - Role: Basic Execution Role
  - Permissions:
    - `sns:Subscribe`
    - `sns:Receive`
    - `ses:SendEmail`
    - `ses:SendRawEmail`
    - `dynamodb:PutItem`

### Simple Notification Service (SNS)
- An SNS topic has been created.
- The Lambda function is subscribed to this SNS topic.
- SNS is configured as a triggering point for the Lambda function.

### EC2 Userdata
- SNS Region and ARN are passed in the EC2 userdata.
- This allows the application running on EC2 instances to access SNS.

## Hosted Zone

- Description: The hosted zone configuration for mapping subdomains to instance IPs.

### A Records

- Subdomain: dev.pramod.cloud / demo.pramod.cloud

## SSL Certificate Import to ACM - Command

### Switch to Demo Profile
- set AWS_PROFILE="demo"

### Command to import
- aws acm --profile=demo import-certificate --certificate fileb://C:/Users/pramo/Desktop/ssl/demo_pramod_cloud.crt --certificate-chain fileb://C:/Users/pramo/Desktop/ssl/demo_pramod_cloud.ca-bundle --private-key fileb://C:/Users/pramo/Desktop/ssl/private.key

## Prerequisites
1. Install Python on your local system
2. Install Pulumi on your local system
3. Setup an AWS account
4. Install AWS CLI and setup a profile in your local system
5. Clone this repo in you local system and go inside that directory

## How to set up the pulumi environment before executing
Run the following commands:
1. python -m venv venv
2. venv\Scripts\activate
3. pip install -r requirements.txt
4. pulumi plugin install
5. pulumi stack init [stack_name]
6. pulumi stack select [stack_name]

## How to create resources (executing pulumi)
1. pulumi up


Once "pulumi up" is run, the aforementioned resources would be created using the default variables.

## CLI Commands
In order to create the above network stack using self-defined variables, you may customize the command mentioned below and run it:

pulumi config set <key> <value>

Example:
pulumi config set aws:profile dev ; pulumi config set aws:region us-east-1 ; pulumi config set vpc_name My-VPC1 ; pulumi config set vpc_cidr 10.200.0.0/16 ; pulumi config set public_subnets_cidr '[ "10.200.1.0/24", "10.200.2.0/24", "10.200.3.0/24" ]' ; pulumi config set private_subnets_cidr '[ "10.200.4.0/24", "10.200.5.0/24", "10.200.6.0/24" ]' ; pulumi config set instance_name MyInstance ; pulumi config set ami_id ami-0e58206c8b17a9a3c ; pulumi config set keypair_name mykey ; pulumi config set num_instances 1 ; pulumi config set instance_type t2.micro ; pulumi config set ebs_size 25 ; pulumi config set ebs_type gp2 ; pulumi config set delete_on_termination True ; pulumi config set accidental_termination False ; pulumi config set associate_public_ip True ; pulumi config set security_group_name "application security group"


You can replace with custom values in cli
or you can directly change the custom values in variables.py and then run "pulumi up"

Note 1: If you provide variables via the CLI, the default values will be overridden.

## How to destroy resources ?
Run the following command:
1. pulumi destroy

## How to delete the stack ?
1. pulumi stack rm [stack_name]

If you have created resources using custom variables, make sure to pass the variables as well with the above command

Note: If you're using custom variables, please ensure that vpc_cidr, public_subnet_cidr and private_subnets_cidr values are from the same subnet.

## How to create multiple infrastructures using pulumi ?
You can use pulumi stacks, commands are:
1. pulumi stack init [stack_name]
2. pulumi stack select [stack_name]

(stacks can be dev, prod, test, demo)
