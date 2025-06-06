#Delete a Single File from S3
import boto3

# Initialize S3 client
s3 = boto3.client('s3')

# Define bucket name and file to delete
bucket_name = "my-python-project-bkt-0011"  # Replace with your bucket name
file_key = "uploads/example.txt"  # Replace with the file path in S3

# Delete the file
s3.delete_object(Bucket=bucket_name, Key=file_key)

print(f"File '{file_key}' deleted from S3 bucket '{bucket_name}' successfully!")



#Delete All Files in an S3 Bucket
import boto3

# Initialize S3 resource
s3 = boto3.resource('s3')

# Define the bucket name
bucket_name = "my-python-project-bkt-0011"  # Replace with your bucket name

# Select the bucket
bucket = s3.Bucket(bucket_name)

# Delete all objects in the bucket
bucket.objects.all().delete()

print(f"All files deleted from bucket '{bucket_name}'.")



#Delete the Entire S3 Bucket
import boto3

# Initialize S3 client
s3 = boto3.client('s3')

# Define the bucket name
bucket_name = "my-python-project-bkt-0011"  # Replace with your bucket name

# Delete the bucket
s3.delete_bucket(Bucket=bucket_name)

print(f"S3 bucket '{bucket_name}' deleted successfully!")
