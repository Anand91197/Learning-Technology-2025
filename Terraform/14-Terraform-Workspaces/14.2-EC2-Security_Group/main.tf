#Provider
provider "aws" {
  region = var.region
}

#Security Group
resource "aws_security_group" "env_sg" {
  name        = "sg_${terraform.workspace}"
  description = "Security group for ${terraform.workspace}"
  

  dynamic "ingress" {
    for_each = terraform.workspace == "prod" ? [22, 443] : [22, 80]

    content {
      from_port   = ingress.value
      to_port     = ingress.value
      protocol    = "tcp"
      cidr_blocks = ["0.0.0.0/0"]
    }
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "sg_${terraform.workspace}"
  }
}


#EC2
resource "aws_instance" "ec2_instance" {
  ami                    = var.ami_id
  instance_type          = var.instance_type
  key_name               = var.key_name
  security_groups= ["${aws_security_group.env_sg.name}"]
  tags = {
    Name        = "ec2-${terraform.workspace}"
    Environment = terraform.workspace
  }

  user_data = <<-EOF
              #!/bin/bash
              echo "Hello from ${terraform.workspace}!" > /var/www/html/index.html
              yum update -y
              yum install -y httpd
              systemctl start httpd
              systemctl enable httpd
              EOF
}
