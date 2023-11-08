import pulumi
from pulumi_aws import cloudwatch
from variables import *

# CloudWatch Log Group
log_group = cloudwatch.LogGroup('csye6225',
                                name=log_group_name)

# CloudWatch Log Stream
log_stream = cloudwatch.LogStream('webapp',
                                  name=log_stream_name,
                                  log_group_name=log_group.name)