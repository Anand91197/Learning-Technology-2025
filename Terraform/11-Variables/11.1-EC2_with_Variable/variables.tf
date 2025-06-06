#Define Inputs
variable "region" {
  description = "AWS region"
  default     = "ap-south-1"
}

variable "instance_type" {
  description = "EC2 instance type"
  default     = "t2.micro"
}

variable "ami_value" {
    description = "AMI for EC2"
    default     = "ami-0af9569868786b23a"
}

variable "key_name" {
  description = "Name of the existing key pair"
  type        = string
}