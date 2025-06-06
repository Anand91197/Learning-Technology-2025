#Provider
provider "aws" {
  region = "ap-south-1"
}

#EC2
resource "aws_instance" "my_ec2" {
  ami = "ami-0af9569868786b23a"
  instance_type = "t2.micro"
  key_name = "aws_terraform"

    tags = {
    Name = "Remote-S3"
  }
}


#This is only for lock the state file
/*
resource "aws_s3_bucket" "s3_bucket" {
  bucket = "abhishek-s3-demo-xyz" # change this
}

resource "aws_dynamodb_table" "terraform_lock" {
  name           = "terraform-lock"
  billing_mode   = "PAY_PER_REQUEST"
  hash_key       = "LockID"

  attribute {
    name = "LockID"
    type = "S"
  }
}
*/