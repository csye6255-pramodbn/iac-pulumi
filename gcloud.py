import pulumi
from pulumi_gcp import storage, serviceaccount, iam, projects
import pulumi_gcp as gcp
from variables import *
import json
import pulumi_aws as aws

# Create GCS bucket
bucket = storage.Bucket(gcp_bucket_name,
    location=gcp_bucket_location, # US
    force_destroy=bucket_force_destroy, # True
)

# Create service account
gcp_service_account = serviceaccount.Account(gcp_service_account_name,
   account_id=gcp_service_account_name,   # "my-service-account"                               
   display_name=gcp_service_display_account_name) # "My Storage Admin Service Account"

# Allow service account to upload objects
gcp_bucket_iam = storage.BucketIAMMember('bucket-admin',
    bucket=bucket.name,
    role="roles/storage.admin",
    member=pulumi.Output.concat("serviceAccount:", gcp_service_account.email))

# Create access key
gcp_access_key = serviceaccount.Key('my-access-key',
   service_account_id=gcp_service_account.name,
   public_key_type='TYPE_X509_PEM_FILE')

pulumi.export('service_account_key', gcp_access_key.private_key)