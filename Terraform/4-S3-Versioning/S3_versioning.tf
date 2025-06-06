#Enable Versioning of S3 bucket:

provider "aws" {
    region = "ap-south-1"  
}

#Specific bucket    
resource "aws_s3_bucket_versioning" "versioning_my_s3_bucket" {
  bucket = "tf-anand-sre"
  versioning_configuration {
    status = "Enabled"
  }
  
}

#To apply for all available buckets; Most important, if bucket list are present in the terraform state file then only can use it, otherwise need to mention the bucket name.
/*
resource "aws_s3_bucket_versioning" "versioning_my_s3_bucket" {
  bucket = aws_s3_bucket.my_s3_bucket.id
  versioning_configuration {
    status = "Enabled"
  }
  
}
*/
