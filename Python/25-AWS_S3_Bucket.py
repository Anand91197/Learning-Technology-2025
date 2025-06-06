#/Users/asaini/.aws/credentials > Save Access key
#Install Modules: pip install boto3   #sudo pip install --user boto3
#Run the command to access AWS: aws configure

import boto3

s3 = boto3.client("s3") # Create an S3 client/Initializes the S3 client.

respose = s3.create_bucket(
    Bucket = "anand-primary-bket",
)

####>Bucket create
import boto3

# Initialize S3 client
s3 = boto3.client('s3')

# Bucket name (must be globally unique)
bucket_name = "my-main-bkt"

# Create S3 bucket
response = s3.create_bucket(
    Bucket=bucket_name,
)

print(f"Bucket {bucket_name} created successfully!")






#####List buckets
import boto3

# Create an S3 client
s3 = boto3.client("s3")

# List all buckets
response = s3.list_buckets()

# Print bucket names
for bucket in response["Buckets"]:
    print(bucket["Name"])



#####
##Upload a File to S3
import boto3

# Initialize S3 client
s3 = boto3.client('s3')

# Define bucket name and file details
bucket_name = "my-unique-bucket-data"  # Replace with your bucket name
file_name = "example.txt"  # File to upload (must exist in the same folder as this script)
s3_key = "uploads/example.txt"  # S3 object key (folder structure in S3)

# Upload file to S3
s3.upload_file(file_name, bucket_name, s3_key)

print(f"File '{file_name}' uploaded to S3 bucket '{bucket_name}' successfully!")


##Delete Bucket
#Empty
import boto3

# Initialize S3 client
s3 = boto3.client('s3')

# Define the bucket name
bucket_name = "my-unique-bucket-data"  # Replace with your bucket name

# Delete the empty S3 bucket
s3.delete_bucket(Bucket=bucket_name)

print(f"Bucket '{bucket_name}' deleted successfully!")



#Non-Empty
import boto3

# Initialize S3 resource
s3 = boto3.resource('s3')

# Define the bucket name
bucket_name = "my-unique-bucket-data"  # Replace with your bucket name

# Select the bucket
bucket = s3.Bucket(bucket_name)

# Delete all objects in the bucket
bucket.objects.all().delete()

# Delete the bucket
bucket.delete()

print(f"Bucket '{bucket_name}' and all its contents deleted successfully!")
