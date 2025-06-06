provider "aws" {
  region = "ap-south-1"
}

module "ec2_instance" { 
  source = "/Users/anasaini/Documents/Learning_2025/Terraform/12-Modules/modules/ec2_instance"
  ami_id = "ami-0af9569868786b23a" 
  instance_type = "t2.micro"
  key_name = "aws_terraform"
  region = "ap-south-1"
}