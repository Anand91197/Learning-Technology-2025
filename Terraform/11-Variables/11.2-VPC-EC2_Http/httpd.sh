#!/bin/bash
sudo yum update -y
sudo yum install -y httpd
sudo systemctl start httpd
sudo systemctl enable httpd
echo "<h1>Hello World..! This is Anand Saini and its deployed from Terraform EC2!</h1>" > /var/www/html/index.html
         