django-personal-website
=======================

Template for making a personal website using django. Includes set up of a home page and publications page. Instructions given on how to create additional pages and how to serve it from Amazon.

=======================
Set up instructions
(These instructions assume you are on a fresh machine (e.g. booting up a new Amazon EC2 instance) from which you will serve your site.)

=======================
Log into your computer.

If you are using Amazon:
1. Launch an Amazon EC2 instance running Linux. Micro instances from the free tier are fine. If you don't have a key pair already, create one.
2. Make sure your private key (.pem file) has permissions (chmod 400 my_key.pem)
3. ssh into the instance: ssh -i my_key.pem ec2-user@<aws_ec2_instance_dns>
4. Run "sudo yum update" to make sure all packages are up to date.

=======================
Requirements

1. Install MySQL
# Install it
sudo yum install mysql mysql-server
# Start MySQL
sudo /etc/init.d/mysqld start
# Configure username and password
mysqladmin -u root password yourrootsqlpassword

2. Install Apache and mod_python
sudo yum install mod_python

3. Install django
sudo yum install Django MySQL-python

4. Install git (so you can clone this repository)
sudo yum install git

=======================
Database set up

=======================
Get template code

```
git clone https://github.com/mgymrek/django-personal-website.git
```





