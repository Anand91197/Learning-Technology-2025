Task:- 
Ansible role to install and configure NGINX, serve a basic website (index.html), and start the service.

Goal:-
Role name: nginx

Tasks:

Install nginx

Start and enable nginx

Copy index.html to /usr/share/nginx/html/index.html

ansible-nginx-role/
├── inventory.ini
├── nginx-playbook.yml
└── roles/
    └── nginx/
        ├── tasks/
        │   └── main.yml
        ├── files/
        │   └── index.html
        ├── handlers/
        │   └── main.yml
        ├── defaults/
        │   └── main.yml
        └── meta/
            └── main.yml


1. Create the Role:
ansible-galaxy init roles/nginx

2. Add Your Static Website
📄 roles/nginx/files/index.html

3. Define Tasks
📄 roles/nginx/tasks/main.yml

4. Handlers
📄 roles/nginx/handlers/main.yml

5. Defaults (Optional) ## You can define default vars here (e.g., port, custom file, etc.)
📄 roles/nginx/defaults/main.yml

6. Main Playbook
📄 nginx-playbook.yml

7. Inventory
📄 inventory.ini

Run the Playbook
ansible-playbook -i inventory.ini nginx-playbook.yml

====

Task:- 
Ansible role for Docker installation and running a custom Docker image

Goal for Docker Role
Role name: docker

Tasks:

Install Docker
Start and enable Docker service
Pull custom Docker image from Docker Hub
Run a container


ansible-docker-role/
├── inventory.ini
├── docker-playbook.yml
└── roles/
    └── docker/
        ├── tasks/
        │   └── main.yml
        ├── handlers/
        │   └── main.yml
        ├── defaults/
        │   └── main.yml
        ├── meta/
        │   └── main.yml
        └── README.md


1. Generate the Role
ansible-galaxy init roles/docker


2. Set Default Variables
📄 roles/docker/defaults/main.yml

3. Main Tasks
📄 roles/docker/tasks/main.yml

🧩 Note: This uses community.docker collection. Install it once with:
ansible-galaxy collection install community.docker

4. Handlers
📄 roles/docker/handlers/main.yml


5. Metadata
📄 roles/docker/meta/main.yml

6. Playbook
📄 docker-playbook.yml

7. Inventory
📄 inventory.ini

Run It
ansible-playbook -i inventory.ini docker-playbook.yml
==

(Optional) Prepare for Galaxy Upload:-
To publish this role on Ansible Galaxy:

1. Create a GitHub repo named ansible-role-docker

2. Push this role into it

3. Sign up or log in to https://galaxy.ansible.com

4. Import the role from your GitHub repo

📘 Galaxy expects the role name to be in format: username.rolename (e.g., yourname.docker)
============
>> Push Your Role to GitHub
cd <role-name>
git init
git remote add origin <https://github.com/your_github_username/my_role.git>
git add .
git commit -m "Initial commit"
git push -u origin main
==
Import the Role to Ansible Galaxy:
ansible-galaxy role import <your_github_username> <role-name>
=====