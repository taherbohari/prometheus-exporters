Install MongoDB on Ubuntu 16.04

Step 1 - Importing the Public Key

GPG keys of the software distributor are required by the Ubuntu package manager apt (Advanced Package Tool) to ensure package consistency and authenticity. Run this command to import MongoDB keys to your server.

sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927
--------------------------------------------------------------
Step 2 - Create source list file MongoDB

Create a MongoDB list file in /etc/apt/sources.list.d/ with this command:

echo "deb http://repo.mongodb.org/apt/ubuntu "$(lsb_release -sc)"/mongodb-org/3.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.2.list
--------------------------------------------------------------
Step 3 - Update the repository

update the repository with the apt command:

sudo apt-get update
--------------------------------------------------------------
Step 4 - Install MongoDB

Now you can install MongoDB by typing this command:

sudo apt-get install -y mongodb-org
--------------------------------------------------------------
We have to create a new mongodb systemd service file in the '/lib/systemd/system' directory. Go to that directory and create the new mongodb service file 'mongod.service' with vim.

cd /lib/systemd/system/
vim mongod.service

Paste script below:

[Unit]
Description=High-performance, schema-free document-oriented database
After=network.target
Documentation=https://docs.mongodb.org/manual

[Service]
User=mongodb
Group=mongodb
ExecStart=/usr/bin/mongod --quiet --config /etc/mongod.conf

[Install]
WantedBy=multi-user.target
Save the file and exit.

Now update the systemd service with command below:

systemctl daemon-reload

Start mongodb and add it as service to be started at boot time:

systemctl start mongod
systemctl enable mongod

Now check that mongodb has been started on port 27017 with the netstat command.

netstat -plntu