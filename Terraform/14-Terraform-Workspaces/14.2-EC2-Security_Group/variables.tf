variable "region" {
  description = "AWS region"
  default     = "ap-south-1"
}

variable "ami_id" {
  description = "AMI ID"
  default     = "ami-0af9569868786b23a" # Amazon Linux 2
}

variable "instance_type" {
  description = "EC2 instance type"
  default     = "t2.micro"
}

variable "key_name" {
  description = "SSH key pair name"
  type        = string
}
