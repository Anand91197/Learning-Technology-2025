output "instance_public_ip" {
  value = aws_instance.my_EC2.public_ip
}