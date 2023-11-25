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

# Audit Log Group
audit_log_group = cloudwatch.LogGroup('audit-group',
                                      name=audit_log_group_name)

# Audit Log Stream
audit_log_stream = cloudwatch.LogStream('audit-stream',
                                        name=audit_log_stream_name,
                                        log_group_name=audit_log_group.name)

# # Lambda Log Group
# lambda_log_group = cloudwatch.LogGroup('lambda-group',
#                                        name=lambda_log_group_name)

# # Lambda Log Stream
# lambda_log_stream = cloudwatch.LogStream('lambda-stream',
#                                          name=lambda_log_stream_name,
#                                          log_group_name=lambda_log_group.name)