   provider "aws" {
     region = "ap-south-1"  # Set your desired AWS region
   }

   resource "aws_instance" "my_EC2-Dev" {
     ami           = "ami-0af9569868786b23a"  # Specify an appropriate AMI ID
     instance_type = "t2.micro"
     key_name      = "aws_terraform"
     tags = {
       Name = "Terraform-Dev"
  }
   }



 #Note: Manually, we would need to allow port access from the Security group.
