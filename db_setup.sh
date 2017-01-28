#!/bin/bash

echo "Setting up postgres testdb database..."
echo "==============BEGIN==================="
echo "Creating postgres user named vagrant..."
sudo -u postgres createuser vagrant
echo "Creating postgres database named testdb..."
sudo -u postgres createdb testdb -O vagrant
echo "================END==================="

