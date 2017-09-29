#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from xml.dom import minidom 
import os

IPList = []
nmap_ip = raw_input('\n [+ ]Nmap ip scan: ')
print '\n'
os.system("nmap -sA " + nmap_ip + " -oX nmapOP.xml")
xmldoc = minidom.parse('nmapOP.xml')
hosts = xmldoc.getElementsByTagName('host')
for node in hosts:
    filterCheck = node.getElementsByTagName('extraports')
    for eachCheck in filterCheck:
        check =  eachCheck.getAttribute('state')
        if(check == "unfiltered"):
		    Addr = node.getElementsByTagName('address')
		    for ip in Addr:
		    	if(ip.getAttribute('addrtype')=='ipv4'):
		    	    print str(ip.getAttribute('addr'))
		            IPList.append(str(ip.getAttribute('addr')))
g = open("IPList.txt","w")
for i in IPList:
    g.write(i)
    g.write('\n')
g.close()
