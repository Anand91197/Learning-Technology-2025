variable "region" {
  description = "AWS region"
  default     = "ap-south-1"
}

variable "vpc_cidr" {
  description = "CIDR block for the VPC"
  default     = "10.0.0.0/16"
}

variable "subnet_cidr" {
  description = "CIDR block for the public subnet"
  default     = "10.0.1.0/24"
}

variable "availability_zone" {
  description = "Availability Zone for subnet"
  default     = "ap-south-1a"
}

variable "instance_type" {
  description = "EC2 instance type"
  default     = "t2.micro"
}

variable "ami_id" {
  description = "AMI ID for EC2"
  default     = "ami-0af9569868786b23a" # Amazon Linux 2 in ap-south-1
}

variable "key_name" {
  description = "Key pair name for SSH access"
  type        = string
}
