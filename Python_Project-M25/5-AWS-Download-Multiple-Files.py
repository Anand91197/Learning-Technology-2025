import boto3
import os

# Initialize S3 client
s3 = boto3.client('s3')

# Define the bucket name
bucket_name = "my-python-project-bkt-0011"  # Replace with your bucket name

# Define local folder to store downloaded files
download_folder = "downloaded_files"

# Create folder if it doesn't exist
if not os.path.exists(download_folder):
    os.makedirs(download_folder)

# List all files in the bucket
response = s3.list_objects_v2(Bucket=bucket_name)

# Check if bucket contains files
if 'Contents' in response:
    print(f"Downloading files from S3 bucket '{bucket_name}':")
    
    for obj in response['Contents']:
        s3_file_key = obj['Key']  # S3 file key (path in S3)
        local_file_path = os.path.join(download_folder, os.path.basename(s3_file_key))  # Save with same filename
        
        # Download each file
        s3.download_file(bucket_name, s3_file_key, local_file_path)
        print(f"- Downloaded: {s3_file_key} to {local_file_path}")

    print("All files downloaded successfully!")
else:
    print(f"Bucket '{bucket_name}' is empty.")
