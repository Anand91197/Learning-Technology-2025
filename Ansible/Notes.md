Inventory:- The simplest inventory is a single file with a list of hosts and groups. The default location for this file is /etc/ansible/hosts. You can specify a different inventory source(s) at the command line using the -i <path or expression> option(s) or in using the configuration system.

Default Group:
Even if you do not define any groups in your inventory file, Ansible creates two default groups: all and ungrouped after integrating all inventory sources. The all group contains every host. The ungrouped group contains all hosts that don’t have another group aside from all. Every host will always belong to at least 2 groups (all and ungrouped or all and some other group). For example, in the basic inventory above, the host mail.example.com belongs to the all group and the ungrouped group; the host two.example.com belongs to the all group and the dbservers group. 


Dynamic inventory:-
If your Ansible inventory fluctuates over time, with hosts spinning up and shutting down in response to business demands, the static inventory solutions described in How to build your inventory will not serve your needs. You may need to track hosts from multiple sources: cloud providers, LDAP, Cobbler, and/or enterprise CMDB systems.

Ansible integrates all of these options through a dynamic external inventory system. Ansible supports two ways to connect with external inventory: Inventory plugins and inventory scripts.



Ad hoc commands:

An Ansible ad hoc command uses the /usr/bin/ansible command-line tool to automate a single task on one or more managed nodes. ad hoc commands are quick and easy, but they are not reusable. So why learn about ad hoc commands? ad hoc commands demonstrate the simplicity and power of Ansible.
===

Step-by-Step: Install Ansible on Amazon Linux EC2 - Control-Node

🔸 Step 1: Connect to your EC2 instance
Use SSH to connect:

ssh -i your-key.pem ec2-user@your-ec2-public-ip

🔸 Step 2: Update the system

sudo yum update -y

🔸 Step 3: Install required dependencies

sudo yum install -y python3 pip git

Amazon Linux has Python 3 by default, but this ensures pip and git are also available.

🔸 Step 4: Install Ansible using pip

pip3 install --user ansible
This installs Ansible in your local user directory (~/.local/bin)

🔸 Step 5: Add Ansible to your PATH

echo 'export PATH=$PATH:~/.local/bin' >> ~/.bashrc
source ~/.bashrc

🔸 Step 6: Verify installation

ansible --version


✅ You're done!
Now your EC2 instance can act as a control node.

===
To configure an Ansible Control Node and one or more Managed Nodes:

Control Node:-
Generate an SSH key with a custom name:

ssh-keygen -t rsa -b 4096 -f ~/.ssh/master_node

This will create:

Private key: ~/.ssh/master_node

Public key: ~/.ssh/master_node.pub


Manage-Node:
Then, to copy the key to a remote server:

ssh-copy-id -i ~/.ssh/master_node.pub ec2-user@3.111.31.93 <Public-IP>

And, another way;
Copy this id_rsa.pub key from the Master Node and paste it over Control Node at .ssh/authorized_keys


>Enable Password-Based SSH on EC2:-

Step 1: Connect via Key or EC2 Instance Connect

Step 2: Edit the SSH Config File
sudo vi /etc/ssh/sshd_config
PasswordAuthentication yes
PermitRootLogin yes       # (Optional, if you want root login)
ChallengeResponseAuthentication no

Step 3: Restart SSH Service
sudo systemctl restart sshd

Step 4: Set a Password for Your User
sudo passwd ec2-user
Enter your desired password when prompted.

Step:5 SSH Into EC2 Instance Using Password
ssh ec2-user@3.111.31.93
========================
Why /etc/ansible/ is Missing:
You installed Ansible via pip (Python package manager), not via OS package manager (yum or dnf).

pip installs Ansible without default config directories, like /etc/ansible/.

How to Fix / Create Default Config
If you want to create a config manually:
sudo mkdir -p /etc/ansible
sudo vi /etc/ansible/ansible.cfg


Paste default config content or customize like:
[defaults]
inventory = /etc/ansible/hosts
host_key_checking = False

Create the inventory file:
sudo vi /etc/ansible/hosts
[web]
3.111.31.93 ansible_user=ec2-user ansible_ssh_private_key_file=~/.ssh/master_node

Now Test: ansible all -m ping

===
Install via Yum package

sudo yum update -y

sudo yum install -y python3 pip git

sudo yum install ansible -y

ansible --version

==


cat ~/.ssh/master_node.pub | ssh ec2-user@13.232.206.239 "mkdir -p ~/.ssh && chmod 700 ~/.ssh && cat >> ~/.ssh/authorized_keys && chmod 600 ~/.ssh/authorized_keys"
cat ~/.ssh/master_node.pub | ssh -i ~/.ssh/master_node ec2-user@13.232.206.239 "mkdir -p ~/.ssh && chmod 700 ~/.ssh && cat >> ~/.ssh/authorized_keys && chmod 600 ~/.ssh/authorized_keys"


====
Check Status with Ad-Hoc Command: 
ansible webserver -i inventory.ini -m shell -a "systemctl status httpd"


If want to check yml syntax is perfect then can be run this below command:

ansible-playbook httpd.yml --syntax-check
====

Ansible Roles?
Roles are a way to organize Ansible playbooks into reusable components. They split tasks, variables, files, templates, and handlers into separate structured directories.

Specifce Host for Run:

ansible-playbook copy-ssh.yml -l web2


===
AdHoc

ansible all -m ansible.builtin.service -a "name=httpd state=stopped" -b

ansible all -m ansible.builtin.service -a "name=httpd state=stopped enabled=no" -b

ansible all -m ansible.builtin.package -a "name=httpd state=absent" -b
