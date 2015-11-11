#!/usr/bin/env python

"""
Author: Ronald Osure
2015

"""
import sys
import datetime
import os

def main():
  os.system("cp "+sys.argv[1]+" /tmp/crlpublisher.tmp")
  f = open('/var/log/crlpublisher/crlpublisher.log', 'a')
  data = str(datetime.datetime.now()) + ' - ' + str(sys.argv) + '\n'
  f.write(data)
  f.close()

if __name__ == '__main__':
  main()

