#!/bin/bash
echo "*** Installing Docker"
sudo yum update -y
sudo yum install docker -y
sudo service docker start
docker --version
echo "*** Completed Installation of Docker"
sudo docker run -it --name my_nginx -p8080:80 -d 91197/nginx_custom:1.0
sudo docker run -it --name my_apache -p8081:80 -d 91197/httpd_custom:1.0


#Host port 8080 → Container port 80

