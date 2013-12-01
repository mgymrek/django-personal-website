django-personal-website
=======================

Template for making a personal website using django. Instructions given on how to create additional pages and how to serve it from Amazon.

Special feature is an automatically updating publications page that pulls publications from pubmed using the Biopython library.

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

Get template code
=======================

```
git clone https://github.com/mgymrek/django-personal-website.git
```

Edit pages
=======================

Update **django-personal-website/home/settings.py**
- Under "ADMINS" (line 7) update your name and email address.
- Under "DATABASES" update "NAME" (line 16) to be the name of your MySQL database, and "USER" and "PASSWORD" to be your MySQL username and password.

In **django-personal-website/templates/index.html**
- Change "Your name"
- Add a short description
- Put a .jpg figure you would like on the homepage in ##django-personal-website/pictures/##. Replace "smiley.jpg" with the filename.

In **django-personal-website/templates/publications/index.html**
- Change "Your name"
- Change "My Last name"

In **django-personal-website/templates/publications/article.html**
- Change "Your name"

In **django-personal-website/publications/utils.py**:
- Change "your name" to your name. This will search pubmed for publications with your name on them.

In **django-personal-website/templates/resources.html**
- Change "Your name"


Adding resources
=======================
You can add "resources", and can tie them to publications if you want. For example, if there is supplemental data you want to post that goes along with one of your publications. You can add these through the admin.


Set up database and run locally
=======================

1. Create tables for each app
'''
python manage.py sql publications
python manage.py syncdb
'''

2. Set up all the static files (docs/pictures/css)
```
python manage.py collectstatic
```

3. Run the server (make sure you have port 80 set up to allow http access)
```
sudo python manage.py runserver 0.0.0.0:80
```