import boto3

# Initialize S3 client
s3 = boto3.client('s3')

# Define the bucket name and file details
bucket_name = "my-python-project-bkt-0011"  # Replace with your bucket name
s3_file_key = "uploads/example.txt"  # S3 file path (object key)
local_file_name = "downloaded_example.txt"  # File name to save locally

# Download the file from S3
s3.download_file(bucket_name, s3_file_key, local_file_name)

print(f"File '{s3_file_key}' downloaded from S3 bucket '{bucket_name}' as '{local_file_name}'")
