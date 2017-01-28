# Udacity 299 - Configuring Linux Web Servers

## Objectives
* Use the Apache HTTP Server to respond to HTTP requests and serve a static webpage
* Configure Apache to hand-off specific requests to Python providing the ability to develop dynamic websites
* Setup PostgreSQL and write a simple Python application that generates a data-driven website

## Getting Started
Install [vagrant](https://www.vagrantup.com/docs/getting-started/)

Clone this repository ```$ git clone https://github.com/oharrison/ud299-linux-web-server.git```

```
$ cd ud299-linux-web-server
$ vagrant up
$ vagrant ssh
```
Navigate to ```http://localhost:8080``` in your browser. If you see the "Apache2 Ubuntu Default Page" that means everything's working.

## Configure your firewall
```
# Edit firewall rules
$ nano /vagrant/configure_firewall.sh
# If you've edited or accepted the firewall rules in the file, then run this command to set it all up
$ sh /vagrant/configure_firewall.sh
```

## Disable remote login via password
```
# Change PasswordAuthentication to no
# Uncomment line starting with AuthorizedKeysFile
$ nano /etc/ssh/sshd_config
$ sudo service ssh restart
```

## Generate RSA keys on your host machine
```
$ ssh-keygen
```

## Add your public key on the virtual machine
Copy the contents of your recently generated <key_file>.pub from your host machine into the ~/.ssh/authorized_keys file in your virtual machine.

## Log in the Virtual Machine from your host using SSH 
```
$ ssh -i path/to/private_key vagrant@127.0.0.1 -p YOUR_SSH_PORT_NUMBER
```

## Work with Apache Web Server
```
# Own the html folder so that you can make changes to files
$ sudo chown -R vagrant /var/www/html
```
Configure Apache to handle requests using the WSGI module. Look at the WSGI_Instructions.md file for how to edit this file
```
$ sudo nano /etc/apache2/sites-enabled/000-default.conf
```
Restart the apache service
```
$ sudo apache2ctl restart
```
Create and edit ```/var/www/html/app.wsgi```. Look at the WSGI_Instructions.md file for what to add to this file
```
$ nano /var/www/html/app.wsgi
```
## Work with a database
Checkout this quick and dirty way of setting up and using a db on your new web server.
```
# Create database user and database
# Feel free to edit the username and db name in the /vagrant/db_setup.sh and /vagrant/populate_db.py files before executing thes command
$ sh /vagrant/db_setup.sh
```
Set a password for your newly created user
```
$ psql testdb
testdb=> ALTER USER "vagrant" WITH PASSWORD 'secret';
testdb=> \q
```
Edit this file to include the following line: ```local     all     vagrant    md5```
```
$ sudo nano /etc/postgresql/<version_number>/main/pg_hba.conf
```
Resart the postgresql service
```
$ sudo service postgresql restart
```
Add a table and populate it in the database
```
$ python /vagrant/populate_db.py
```
