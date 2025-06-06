#Terminate
import boto3

# Initialize EC2 client
ec2 = boto3.client('ec2')

# Define the instance ID
instance_id = "i-00adb04aacb1a5e1a"  # Replace with your instance ID

# Terminate the instance
response = ec2.terminate_instances(InstanceIds=[instance_id])

print(f"EC2 Instance {instance_id} is terminating...")