import pulumi
from pulumi_aws import iam, ec2

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

# Create an EC2 instance profile and attach the role
instance_profile = iam.InstanceProfile(
    "myInstanceProfile",
    role=role.name
)
