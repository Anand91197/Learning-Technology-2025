#Define Inputs
variable "region" {
  description = "AWS region"
 
}

variable "instance_type" {
  description = "EC2 instance type"

}

variable "ami_id" {
    description = "AMI for EC2"

}

variable "key_name" {
  description = "Name of the existing key pair"
  type        = string
}