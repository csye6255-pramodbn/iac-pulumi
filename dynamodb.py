import pulumi
import pulumi_aws as aws
from pulumi_aws import dynamodb
from variables import *

# Creating the DynamoDB table.
dynamodb_table = dynamodb.Table(dynamodb_table_name,
    attributes=[
        {"name": "ID", "type": "S"},
        {"name": "Name", "type": "S"},
        {"name": "Email", "type": "S"},
        {"name": "Timestamp", "type": "S"},
        {"name": "Status", "type": "S"},
        {"name": "StatusDetails", "type": "S"}
    ],
    hash_key="ID",
    read_capacity=5,
    write_capacity=5,
    global_secondary_indexes=[
        {
            "name": "NameIndex",
            "hashKey": "Name",
            "projectionType": "ALL",
            "readCapacity": 5,
            "writeCapacity": 5
        },
        {
            "name": "EmailIndex",
            "hashKey": "Email",
            "projectionType": "ALL",
            "readCapacity": 5,
            "writeCapacity": 5
        },
        {
            "name": "TimestampIndex",
            "hashKey": "Timestamp",
            "projectionType": "ALL",
            "readCapacity": 5,
            "writeCapacity": 5
        },
        {
            "name": "StatusIndex",
            "hashKey": "Status",
            "projectionType": "ALL",
            "readCapacity": 5,
            "writeCapacity": 5
        },
        {
            "name": "StatusDetailsIndex",
            "hashKey": "StatusDetails",
            "projectionType": "ALL",
            "readCapacity": 5,
            "writeCapacity": 5
        }
    ]
)

dynamodb_table_name = dynamodb_table.name
dynamodb_table_arn = dynamodb_table.arn