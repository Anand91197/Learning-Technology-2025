import boto3

# Initialize S3 client
s3 = boto3.client('s3')

# Define bucket name
bucket_name = "my-python-project-bkt-0011"  # Change this to your bucket name

# List all objects in the bucket
response = s3.list_objects_v2(Bucket=bucket_name)


# Check if bucket is empty
if 'Contents' in response:
    print(f"Files in bucket '{bucket_name}':")
    for obj in response['Contents']:
        print(f"- {obj['Key']} (Size: {obj['Size']} bytes)")
else:
    print(f"Bucket '{bucket_name}' is empty.")

