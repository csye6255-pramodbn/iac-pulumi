## Name : Pramod Begur Nagaraj
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

## Prerequisites
1. Install pulumi on your local system
2. Setup an AWS account
3. Install AWS CLI and setup a profile in your local system
4. Clone this repo in you local system and go inside that directory


## How to set up the pulumi environment before executing
Run the following commands:
1. python -m venv venv
venv\Scripts\activate
2. pip install -r requirements.txt
3. pulumi plugin install
4. pulumi stack init [stack_name]
5. pulumi stack select [stack_name]

## How to create resources (executing pulumi)
1. pulumi up


Once "pulumi up" is run, the aforementioned resources would be created using the default variables.

In order to create the above network stack using self-defined variables, you may customize the command mentioned below and run it:

pulumi config set profile dev region us-west-2 vpc_name My-VPC vpc_cidr 10.1.0.0/16 public_subnet_cidr 10.1.1.0/24,10.1.2.0/24,10.1.3.0/24 private_subnet_cidr 10.1.4.0/24,10.1.5.0/24,10.1.6.0/24

You can replace with custom values 
or you can directly change the custom values in variables.py and then run "pulumi up"

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