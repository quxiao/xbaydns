#!/usr/bin/env python
# encoding: utf-8
"""
logtolist.py

Created by QingFeng on 2008-03-16.
Copyright (c) 2008 xBayDNS Team. All rights reserved.
"""
import re, sys

def logtolist(s):
    data={}
    c=re.compile("client (\d+\.\d+\.\d+\.\d+)#")
    for ip in c.findall(s):
        data[ip]=''
    return data.keys()

def genlist(logfile, iplist):
    log = open(logfile, "r").read()
    ips = logtolist(log)
    iplistfile = open(iplist, "w")
    for ip in ips:
        iplistfile.write("%s\n"%ip)
    iplistfile.close()
    return

def main():
    if len(sys.argv) != 3:
        print "Usage: %s logfile outputfile"%__file__
        sys.exit(1)
    genlist(sys.argv[1], sys.argv[2])
	
if __name__ == "__main__":
    main()
