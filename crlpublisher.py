#!/usr/bin/env python

"""
Author: Ronald Osure
2015

"""
import sys
import datetime
import os
import ConfigParser

CONFIG_FILE = '/etc/crlpublisher/crlpublisher.conf'

def main():
  config = ConfigParser.RawConfigParser()
  config.read(CONFIG_FILE)

  # Delete the old CRL file. The reason for manual delete is because scp doesn't overwrite a file when you specify the target file name in the scp commnad

  os.system("ssh -i %s %s@%s rm %s" % (config.get('local','identityFile'), config.get('remote','remoteUser'),config.get('remote','remoteHost'),config.get('remote','remoteLocation')))

  # We can now copy the file over

  os.system("scp -i %s %s %s@%s:%s" % (config.get('local','identityFile'), sys.argv[1], config.get('remote','remoteUser'),config.get('remote','remoteHost'),config.get('remote','remoteLocation')))

  #Log event
  f = open(config.get('local','logFile'), 'a')
  data = str(datetime.datetime.now()) + ' - ' + str(sys.argv) + '\n'
  f.write(data)
  f.close()

if __name__ == '__main__':
  main()

