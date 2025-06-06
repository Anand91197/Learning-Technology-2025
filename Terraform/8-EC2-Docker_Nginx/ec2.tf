#EC2_Instance
resource "aws_instance" "web_instance" {
  ami                    = "ami-0af9569868786b23a" # Amazon Linux 2 
  instance_type          = "t2.micro"
  key_name               = "aws_terraform"   # Replace with your key pair
  vpc_security_group_ids = [aws_security_group.web_sg.id]
  user_data              = base64encode(file("userdata.sh"))

  tags = {
    Name = "WebInstance"
  }
}

#Output
output "ec2_public_ip" {
  description = "Public IP of EC2 instance"
  value       = aws_instance.web_instance.public_ip
}