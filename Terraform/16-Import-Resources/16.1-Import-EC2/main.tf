provider "aws" {
  region = "ap-south-1"
}

resource "aws_instance" "my_ec2" {
  # Placeholder values - these will be updated after import
  ami           = "ami-12345678" #ami-0f535a71b34f2d44a
  instance_type = "t2.micro"
}
