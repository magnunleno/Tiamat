#!/usr/bin/env python3
# encoding: utf-8

from difflib import SequenceMatcher

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
    def listAllHostnames(self):
        pass

    @classmethod
    def saveHost(self):
        pass

    @classmethod
    def deleteHost(self):
        pass

    @classmethod
    def searchHost(self, hostname, top=5):
        hosts = self.listAllHostnames()
        hosts = sorted(hosts,
            key=lambda x : SequenceMatcher(None, hostname, x).ratio(),
            reverse=True)
        return hosts[:top]

    def connect(self):
        pass
