from pulumi import Config
import pulumi_aws as aws

config = Config("aws")
aws_profile = config.get("profile")
provider = aws.Provider("provider", profile=aws_profile)
