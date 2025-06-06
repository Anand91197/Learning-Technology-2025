provider "aws" {
    region = "ap-south-1"  # Set your desired AWS region
}
resource "aws_s3_bucket" "my_s3_bucket" {
  bucket = "tf-anand-sre"
}
