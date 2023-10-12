from pulumi import Config
import pulumi_aws as aws
config1 = Config("aws")

aws_profile = config1.get("profile")

provider = aws.Provider("provider", profile=aws_profile)