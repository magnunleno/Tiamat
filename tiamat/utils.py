#!/usr/bin/env python3
# encoding: utf-8

import re
import socket
import dns.resolver

from os import mkdir
from os.path import expanduser
from os.path import exists
from os import sep

IP_RE = re.compile("^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$")

root = sep.join([expanduser("~"), ".tiamat"])
if not exists(root):
    mkdir(root)

def decodeHost(host):
    user = None
    port = None
    if "@" in host:
        (user, host) = host.split('@')
    if ':' in host:
        (host, port) = host.split(':')
    return (user, host, port)

def isIP(host):
    return IP_RE.match(host)

def getSSHString(host):
    (user, host, port) = decodeHost(host)
    if user:
        conn_str = "ssh %s@%s"%(user, host)
    else:
        conn_str = "ssh %s"%(host)
    if port:
        conn_str += " -p " + port
    return conn_str

def getFTPString(host):
    (user, host, port) = decodeHost(host)
    if port:
        return "ftp %s %s "%(host, port)
    return "ftp %s"%(host)

def getTelnetString(host):
    (user, host, port) = decodeHost(host)
    if user:
        conn_str = "telnet -l %s %s"%(user, host)
    else:
        conn_str = "telnet %s"%(host)
    if port:
        conn_str += " " + port
    return conn_str

def getHostByName(host):
    try:
        (host, aliases, addresses) = socket.gethostbyname_ex(host)
    except socket.gaierror:
        print "Unknown host: %s"%host
        exit(1)
    print "Host:"
    print "    %s"%host
    print "Aliases:"
    if aliases:
        for alias in aliases:
            print '    %s'%alias
    else:
        print "    None"
    print "Addresses:"
    if addresses:
        for address in addresses:
            print "    %s"%address
    else:
        print "    None"
    return (host, aliases, addresses)

def getHostByAddress(host):
    try:
        host, aliases, addresses = socket.gethostbyaddr(host)
    except socket.gaierror:
        print "Unknown host: %s"%host
        exit(1)
    print "Host:"
    print "    %s"%host
    print "Aliases:"
    if aliases:
        for alias in aliases:
            print '    %s'%alias
    else:
        print "    None"
    print "Addresses:"
    if addresses:
        for address in addresses:
            print "    %s"%address
    else:
        print "    None"
    return (host, aliases, addresses)

def getDNSLookUp(host, dns_server):
    resolver = dns.resolver.Resolver()
    if dns_server:
        resolver.nameservers = [dns_server]
        print "# Lookup for %s in %s"%(host, dns_server)
    else:
        print "# Lookup for %s"%(host)
    try:
        answer = resolver.query(host)
    except Exception as e:
        if e.message:
            print "Error during request:",e.message
        else:
            print "Error during request:",e.__repr__().split('(')[0]
        exit(1)
    print answer.rrset.to_text()


