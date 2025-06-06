provider "aws" {
    region = "ap-south-1"  # Set your desired AWS region
}
resource "aws_iam_user" "my_iam_user" {
    name = "test_user_terraform"
  
}

#Multiple IAM User
resource "aws_iam_user" "my_iam_users" {
    count = 2
    name = "test_user_terraform.${count.index}"
  
}