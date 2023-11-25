import pulumi
from pulumi_aws import lambda_
from variables import *
from iam_policy import *
from gcloud import *
import pulumi_aws as aws
import json
from dynamodb import *

# Create Lambda function with NodeJS 14.x runtime
lambda_func = lambda_.Function(lambda_name,
    runtime= "nodejs16.x",
    handler="index.lambdaHandler",
    role=lambda_policy_arn,
    code=pulumi.AssetArchive({
      '.': pulumi.FileArchive('./serverless')
   }),

    environment={
        "variables": {
            "GCP_CREDENTIALS": gcp_access_key.private_key.apply(lambda key: key),
            "GCP_BUCKET_NAME": bucket.name,
            "DYNAMODB_TABLE_NAME": dynamodb_table.name,
        },
    },
)
lambda_arn = lambda_func.arn