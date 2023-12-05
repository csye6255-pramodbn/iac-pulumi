import pulumi
from pulumi_aws import sns
from variables import *
from aws_lambda import *
from iam_policy import *


# Create an SNS topic
sns_topic = sns.Topic(sns_topic_name, name=sns_topic_name)
topic_arn = sns_topic.arn

# store the sns region in a variable
sns_region = sns_topic.arn.apply(lambda arn: arn.split(":")[3])

# Create an SNS subscription for lambda function
subscription = sns.TopicSubscription(sns_subscription_name,
    topic=topic_arn,
    protocol='lambda',
    endpoint=lambda_arn,
)

# Setting Trigger for Lambda function
invoke = lambda_.Permission('invokelambda',
    action='lambda:InvokeFunction',
    principal='sns.amazonaws.com',
    source_arn=topic_arn,
    function=lambda_func
)