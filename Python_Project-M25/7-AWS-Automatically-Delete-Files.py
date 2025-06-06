import boto3
import json

# Initialize S3 client
s3 = boto3.client('s3')

# Define bucket name
bucket_name = "my-unique-bucket-123456789"  # Replace with your bucket name

# Define the lifecycle policy
lifecycle_policy = {
    "Rules": [
        {
            "ID": "DeleteOldFiles",  # Rule ID
            "Prefix": "uploads/",  # Apply to all files under 'uploads/' folder
            "Status": "Enabled",
            "Expiration": {"Days": 30},  # Delete files older than 30 days
        }
    ]
}

# Apply the lifecycle policy
s3.put_bucket_lifecycle_configuration(
    Bucket=bucket_name,
    LifecycleConfiguration=lifecycle_policy
)

print(f"Lifecycle policy applied to bucket '{bucket_name}'. Files older than 30 days will be deleted automatically.")
