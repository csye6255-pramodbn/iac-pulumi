import pulumi
import pulumi_aws as aws
from variables import region, profile

aws_provider = aws.Provider(profile, region = region)



