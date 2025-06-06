import boto3

# Initialize EC2 client
ec2 = boto3.client('ec2')

# Define EC2 parameters
ami_id = "ami-002f6e91abff6eb96"  # Replace with a valid AMI ID
instance_type = "t2.micro"
key_name = "aws_python"  # Replace with your key pair name
security_group = "my-own-SG"  # Replace with your security group name

# Launch an EC2 instance
response = ec2.run_instances(
    ImageId=ami_id,
    InstanceType=instance_type,
    KeyName=key_name,
    SecurityGroups=[security_group],
    MinCount=1,
    MaxCount=1
)

# Get the instance ID
instance_id = response['Instances'][0]['InstanceId']   #Since we created only one instance (MinCount=1, MaxCount=1), we take the first item in the list ([0]).
print(f"EC2 Instance created with ID: {instance_id}")
