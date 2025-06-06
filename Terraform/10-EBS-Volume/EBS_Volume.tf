#Provider
provider "aws" {
    region = "ap-south-1"  
}

#EC2 Instance
resource "aws_instance" "web_instance" {
ami = "ami-0af9569868786b23a"
instance_type = "t2.micro"
key_name = "aws_terraform"
availability_zone="ap-south-1a"

tags = {
    Name = "WebServer"
  }
}




#Create EBS Volume
resource "aws_ebs_volume" "web_volume" {
availability_zone = "ap-south-1a"
size = 5  #Size in GB

tags = {
Name = "Web_EBS"
}
}

#Attaching EBS volume
resource "aws_volume_attachment" "ebs_att" {
device_name = "/dev/xvdf"
volume_id = aws_ebs_volume.web_volume.id
instance_id = aws_instance.web_instance.id
force_detach = true
depends_on = [aws_ebs_volume.web_volume]
}