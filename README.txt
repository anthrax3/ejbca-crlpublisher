~~~~ EJBCA CUSTOM PUBLISHER TO PUSH CRLs to PUBLIC FACING SITE ~~~~~

Author: Ronald Osure
Twitter: @Ever_Sure
Orgnanization: Kenya Education Network Trust

This is a solution that allows the publishing of CRLs to a remote host using EJBCA's General Purpose Custom Publisher

~~~~ INSTALLATION (On Ubuntu 14.04, adjust to suit your environment but commands should work for most Linux distros) ~~~~

# Change directory to project dir
cd ejbca-crlpublisher/
sudo mkdir /etc/crlpublisher

# Copy config file to /etc and the executable python script to /usr/local/bin

sudo cp crlpublisher.conf /etc/crlpublisher
sudo chmod 640 /etc/crlpublisher/crlpublisher.conf
sudo chmod root:ejbca /etc/crlpublisher/crlpublisher.conf

sudo cp crlpublisher.py /usr/local/bin/crlpublisher.py
sudo chmod 750 /usr/local/bin/crlpublisher.py
sudo chown root:ejbca /usr/local/bin/crlpublisher.py

# Update the config file to suit your environment settings

# Setup SSH passwordless login to your remote host. This step is mandatory for everything to work as expected
