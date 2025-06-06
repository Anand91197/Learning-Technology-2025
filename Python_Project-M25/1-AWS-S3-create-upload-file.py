import boto3

# Initialize S3 client
s3 = boto3.client('s3')

# Define bucket name (must be globally unique)
bucket_name = "my-python-project-bkt-0011"  # Change this to a unique name

# Create S3 Bucket
s3.create_bucket(Bucket=bucket_name)

print(f"Bucket '{bucket_name}' created successfully!")

# Upload a file to S3
file_name = "example.txt"  # Replace with your local file
s3_key = "pycode/example.txt"  # S3 object key (folder structure in S3)

s3.upload_file(file_name, bucket_name, s3_key)

print(f"File '{file_name}' uploaded to S3 bucket '{bucket_name}' successfully!")
