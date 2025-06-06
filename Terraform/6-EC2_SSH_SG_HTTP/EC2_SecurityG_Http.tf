#Provider
provider "aws" {
    region = "ap-south-1"  
}

#Security Group
resource "aws_security_group" "my_sg" {
name = "allow_http"
description = "Allow http and ssh inbound traffic"


ingress {
description = "http"
from_port = 80
to_port = 80
protocol = "tcp"
cidr_blocks = ["0.0.0.0/0"]
}
ingress {
description = "ssh"
from_port = 22
to_port = 22
protocol = "tcp"
cidr_blocks = ["0.0.0.0/0"]
}
egress {
from_port = 0
to_port = 0
protocol = "-1" # all protocols
cidr_blocks = ["0.0.0.0/0"]
}

tags = {
Name = "allow_http_ssh"
}
}

#EC2 with HTTP Code
resource "aws_instance" "web_instance" {
ami = "ami-0af9569868786b23a"
instance_type = "t2.micro"
key_name = "aws_terraform"
availability_zone="ap-south-1a"
security_groups= ["${aws_security_group.my_sg.name}"]


user_data = <<-EOF
            #!/bin/bash
            yum update -y
            yum install -y httpd
            systemctl start httpd
            systemctl enable httpd
            echo "<h1>Deployed via Terraform</h1>" > /var/www/html/index.html
            EOF

  tags = {
    Name = "WebServer"
  }
}

output "instance_public_ip" {
  description = "Public IP of the EC2 instance"
  value       = aws_instance.web_instance.public_ip
}