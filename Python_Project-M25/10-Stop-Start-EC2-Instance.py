#ShutDown EC2
import boto3

# Initialize EC2 client
ec2 = boto3.client('ec2')

# Define the instance ID
instance_id = "i-00adb04aacb1a5e1a"  # Replace with your instance ID

# Stop the instance
response = ec2.stop_instances(InstanceIds=[instance_id])

print(f"EC2 Instance {instance_id} is stopping...")



#Start a Stopped EC2 Instance
import boto3

# Initialize EC2 client
ec2 = boto3.client('ec2')

# Define the instance ID (Replace with your stopped instance ID)
instance_id = "i-00adb04aacb1a5e1a"

# Start the instance
response = ec2.start_instances(InstanceIds=[instance_id])

print(f"EC2 Instance {instance_id} is starting...")




