variable "region"          { 
    default = "ap-south-1" 
    }
variable "vpc_cidr"        { 
    default = "10.0.0.0/16" 
    }
variable "subnet_cidr"     { 
    default = "10.0.1.0/24" 
    }
variable "availability_zone" {
     default = "ap-south-1a" 
     }
variable "instance_type"   { 
    default = "t2.micro" 
    }
variable "ami_id"          { 
    default = "ami-0af9569868786b23a" 
    }
variable "key_name"        { 
    type = string 
    }
