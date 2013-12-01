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
sudo yum -y update
```
to make sure all packages are up to date.

Requirements
=======================

1. Install MySQL
```
# Install it
sudo yum -y install mysql mysql-server
# Start MySQL
sudo /etc/init.d/mysqld start
# Configure username and password
mysqladmin -u root password yourrootsqlpassword
```

2. Install Apache and mod_python
```
sudo yum -y install mod_python
```

3. Install django and MySQL-python
```
sudo yum -y install MySQL-python
sudo yum -y install python-pip
sudo pip install django
```

4. Install Biopython (used to automatically update publications page)	
```
sudo yum -y install python26-devel
sudo yum -y install gcc
sudo pip install biopython
```

5. Install git (so you can clone this repository)
```
sudo yum -y install git
```

6. Install other apache/httpd required packages
```
sudo yum -y install httpd-devel
sudo yum -y install mod_wsgi
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

In **django-personal-website/templates/resources/index.html**
- Change "Your name"

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

Adding resources
=======================
You can add "resources", and can tie them to publications if you want. For example, if there is supplemental data you want to post that goes along with one of your publications. You can add these through the admin.

First make sure you have a superuser set up:
```
python manage.py createsuperuser --username=joe --email=joe@example.com
```

Now, go to the django admin page at <ec2-dns:80>/admin. Sign in with the superuser name and password. Here you can manage everything in the database that django draws information from. For instance if you already ran the above steps you should see your publications listed. To add a resource, go to "Add resource".


Adding additional pages
=======================
Information about adding additional pages can be found at https://docs.djangoproject.com.


Additional configuration
=======================
To change the style, edit the CSS file at django-personal-website/css/djangoweb.css. After you change this, be sure to run "collectstatic" again so you can see the changes.


Serving the site
=======================
1. Edit *django-personal-website/httpd.conf*. Put the DNS of your EC2 instance at line 1015.

2. Copy the original httpd.conf file somwhere in case you screw something up
```
sudo cp /etc/httpd/conf/httpd.conf old_httpd.conf
```

3. Copy your httpd.conf to where Apache knows to look for it
```
sudo cp ~/django-personal-website/httpd.conf /etc/httpd/conf/
```

4. Create a logs directory for apache
```
mkdir /home/ec2-user/django-personal-website/logs
```

5. Edit *django-personal-website/apache/django.wsgi*. Change the paths to your django root directory if it is not at /home/ec2-user/django-personal-website.

6. Start httpd
```
sudo /etc/init.d/httpd restart
```

6. Tie your Amazon EC2 instance's DNS to your domain name, for instance at name.com.