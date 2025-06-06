import boto3

# Initialize EC2 client
ec2 = boto3.client('ec2')

# Fetch all running EC2 instances
response = ec2.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])

# Extract instance details
print("Running EC2 Instances:")
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        print(f"- Instance ID: {instance['InstanceId']}, Type: {instance['InstanceType']}, Public IP: {instance.get('PublicIpAddress', 'N/A')}")
