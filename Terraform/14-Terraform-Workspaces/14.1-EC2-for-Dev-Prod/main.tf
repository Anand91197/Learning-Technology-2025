#Provider
provider "aws" {
  region = var.region
}


#EC2
resource "aws_instance" "ec2_instance" {
  ami                    = var.ami_id
  instance_type          = var.instance_type
  key_name               = var.key_name
  
  tags = {
    Name        = "ec2-${terraform.workspace}"
    Environment = terraform.workspace
  }
}
