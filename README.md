django-personal-website
=======================

Template for making a personal website using django. Includes set up of a home page and publications page. Instructions given on how to create additional pages and how to serve it from Amazon.

Set up instructions
=======================
(These instructions assume you are on a fresh machine (e.g. booting up a new Amazon EC2 instance) from which you will serve your site.)

Log into your computer.
=======================

If you are using Amazon:
1. Launch an Amazon EC2 instance running Linux. Micro instances from the free tier are fine. If you don't have a key pair already, create one.

2. Make sure your private key (.pem file) has permissions
```
chmod 400 my_key.pem
```

3. ssh into the instance
```
ssh -i my_key.pem ec2-user@<aws_ec2_instance_dns>
```

4. Run
```
sudo yum update
```
to make sure all packages are up to date.

Requirements
=======================

1. Install MySQL
```
# Install it
sudo yum install mysql mysql-server
# Start MySQL
sudo /etc/init.d/mysqld start
# Configure username and password
mysqladmin -u root password yourrootsqlpassword
```

2. Install Apache and mod_python
```
sudo yum install mod_python
```

3. Install django and MySQL-python
```
sudo yum install MySQL-python
sudo yum install python-pip
sudo pip install django
```

4. Install Biopython (used to automatically update publications page)	
```
sudo yum install python26-devel
sudo yum install gcc
sudo pip install biopython
```

5. Install git (so you can clone this repository)
```
sudo yum install git
```
=======================
Get template code

```
git clone https://github.com/mgymrek/django-personal-website.git
```
=======================
Edit pages

1. Update django-personal-website/home/settings.py
Under "ADMINS" (line 7) update your name and email address.
Under "DATABASES" update "NAME" (line 16) to be the name of your MySQL database, and "USER" and "PASSWORD" to be your MySQL username and password.

2. Edit the homepage
In django-personal-website/templates/index.html:
 Change "Your name"
 Add a short description
 Put a .jpg figure you would like on the homepage in django-personal-website/pictures/. Replace "smiley.jpg" with the filename.

3. Edit publications
In django-personal-website/templates/publications/index.html:
 Change "Your name"
 Change "My Last name"
In django-personal-website/templates/publications/article.html:
 Change "Your name"
In django-personal-website/publications/utils.py:
 Change "your name" to your name. This will search pubmed for publications with your name on them.

4. Edit resources
In django-personal-website/templates/resources.html:
 Change "Your name"
To add "resources":
# TODO
=======================
Set up database

1. Create tables for each app
'''
python manage.py sql publications
python manage.py syncdb
'''


python manage.py collectstatic
sudo python manage.py runserver 0.0.0.0:80