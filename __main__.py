import pulumi
import provider  # Import provider module
opts = pulumi.ResourceOptions(provider=provider.provider) # Pass provider to resource options
import myVPC
import security_group
import instance
import outputs