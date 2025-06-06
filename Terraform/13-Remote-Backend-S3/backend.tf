terraform {
  backend "s3" {
    bucket         = "tf-anand-sre" # change this
    key            = "remote-backend-terraform-91197/terraform.tfstate"
    region         = "ap-south-1"
    encrypt        = true
  }
}


/*
https://developer.hashicorp.com/terraform/language/backend/s3
*/