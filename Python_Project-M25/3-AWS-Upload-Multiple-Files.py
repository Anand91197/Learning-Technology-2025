import boto3
import os

# Initialize S3 client
s3 = boto3.client('s3')

# Define bucket name
bucket_name = "my-python-project-bkt-0011"  # Replace with your bucket name

# Define the local folder containing files to upload
local_folder = "upload_files"  # Replace with your folder name

# Upload all files in the folder
for file_name in os.listdir(local_folder):
    file_path = os.path.join(local_folder, file_name)
    
    # Check if it's a file (not a subdirectory)
    if os.path.isfile(file_path):
        s3_key = f"uploads/{file_name}"  # S3 folder structure
        s3.upload_file(file_path, bucket_name, s3_key)
        print(f"Uploaded: {file_name} to S3 bucket '{bucket_name}'")

print("All files uploaded successfully!")
