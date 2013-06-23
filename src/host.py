#!/usr/bin/env python3
# encoding: utf-8

SERVICES = (
    'ftp',
    'ssh',
    'telnet',
    )

class Host(object):
    __slots__ = (
        'address',
        'hostname',
        'description',
        'active',        
        'user',        
        'service',        
    )

    def __init__(self, hostname, address):
        pass

    @classmethod
    def listHosts(self):
        pass

    @classmethod
    def saveHost(self):
        pass

    @classmethod
    def deleteHost(self):
        pass

    @classmethod
    def searchHost(self):
        pass

    def connect(self):
        pass
