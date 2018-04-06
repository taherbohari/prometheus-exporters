#!/bin/bash -ex

java -version 
java -version 
echo $JAVA_HOME
wget -qO - https://packages.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -
echo "deb http://packages.elastic.co/elasticsearch/5.x/debian stable main" | sudo tee -a /etc/apt/sources.list.d/elasticsearch-5.x.list
sudo apt-get update
sudo apt-get install elasticsearch
sudo update-rc.d elasticsearch defaults
sudo service elasticsearch start
