import pulumi
from pulumi_aws import iam
import pulumi_aws as aws

###################################################################################################################
############################ IAM Policy for EC2 ##############
###################################################################################################################

# Create an IAM role
role = iam.Role(
    "myRole",
    assume_role_policy={
        "Version": "2012-10-17",
        "Statement": [{
            "Action": "sts:AssumeRole",
            "Effect": "Allow",
            "Principal": {
                "Service": "ec2.amazonaws.com"
            },
        }],
    }
)

# Attach the AmazonRDSFullAccess policy to the role
rds_policy_attachment = iam.RolePolicyAttachment(
    "myRDSFullAccessPolicyAttachment",
    policy_arn="arn:aws:iam::aws:policy/AmazonRDSFullAccess",
    role=role.name
)

# Attach the CloudWatchAgentServerPolicy to the role
cloudwatch_policy_attachment = iam.RolePolicyAttachment(
    "myCloudWatchAgentServerPolicyAttachment",
    policy_arn="arn:aws:iam::aws:policy/CloudWatchAgentServerPolicy",
    role=role.name
)

# Attach the SNSFullAccess policy to the role
sns_policy_attachment = iam.RolePolicyAttachment(
    "EC2SNSFullAccessPolicyAttachment",
    policy_arn="arn:aws:iam::aws:policy/AmazonSNSFullAccess",
    role=role.name
)

# Create an EC2 instance profile and attach the role
instance_profile = iam.InstanceProfile(
    "myInstanceProfile",
    role=role.name
)

#######################################################################################################################
############################ IAM Policy for Lambda ##############
#######################################################################################################################


# Create IAM role for Lambda
lambda_role = iam.Role(
    "myLambdaRole",
    assume_role_policy={
        "Version": "2012-10-17",
        "Statement": [{
            "Action": "sts:AssumeRole",
            "Effect": "Allow",
            "Principal": {
                "Service": "lambda.amazonaws.com"
            },
        }],
    }
)

# Attach the AWSLambdaBasicExecutionRole policy to the role
lambda_basic_execution_policy_attachment = iam.RolePolicyAttachment(
    "myLambdaBasicExecutionPolicyAttachment",
    policy_arn="arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole",
    role=lambda_role.name
)


# SNS and SES Policy for Lambda
lambda_sns_ses_policy = aws.iam.Policy("lambda-sns-ses-db-policy",
    description="Policy for Lambda to subscribe and receive SNS and send email via SES and put item in DynamoDB",
    policy={
        "Version": "2012-10-17",
        "Statement": [{
            "Action": [
                "sns:Subscribe",
                "sns:Receive",
                "ses:SendEmail",
                "ses:SendRawEmail",
                "dynamodb:PutItem"
            ],
            "Effect": "Allow",
            "Resource": ["*"]
        }]
    }
)

# Attach the SES Send Policy to the role
lambda_policy_attachment = iam.RolePolicyAttachment("lambda-sns-ses-db-policy-attachment",
    role=lambda_role.name,
    policy_arn=lambda_sns_ses_policy.arn
)

# Assigning lambda policy arn to a variable
lambda_policy_arn = lambda_role.arn

#####################################################################################################################
############################ IAM Policy for SNS ##############
#####################################################################################################################

# # Create IAM role for SNS
# sns_role = iam.Role("sns-publish-role",
#     assume_role_policy={
#         "Version": "2012-10-17",
#         "Statement": [{
#             "Action": "sts:AssumeRole",
#             "Principal": {
#                 "Service": "sns.amazonaws.com"
#             },
#             "Effect": "Allow"
#         }]
#     })

# # Create IAM policy for SNS
# sns_publish_policy = iam.Policy("sns-publish-policy",
#     policy={
#         "Version": "2012-10-17",
#         "Statement": [{
#             "Action": [
#                 "sns:Publish"
#             ],
#             "Effect": "Allow", 
#             "Resource": "*"   
#         }]
#     })

# # Attach the SNS publish policy to the role
# sns_policy_attach = iam.RolePolicyAttachment("sns-attach",
#     role=sns_role.name, 
#     policy_arn=sns_publish_policy.arn
# )

# # Assigning sns policy arn to a variable
# sns_policy_arn = sns_role.arn