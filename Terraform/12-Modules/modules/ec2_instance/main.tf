#Use variables in your resources
provider "aws" {
  region = var.region
}


resource "aws_instance" "my_EC2" {
  ami           = var.ami_id
  instance_type = var.instance_type
  key_name      = var.key_name
  
  tags = {
    Name = "Module_EC2"
  }
}