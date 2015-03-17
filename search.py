# -*- coding: utf-8 -*-
__author__ = 'prance'
import whois
from google import search
import urllib


def colide():

    results = search('aparaty słuchowe dofinansowanie', tld='pl', lang='pl',start=15, stop=40)
    uzyte = []
    for i in results:
        i = str(i)
        end = len(i)-1
        if i[:5] == 'https':
            i = i[8:]
        elif i[:4] == 'http':
            i = i[7:]
        domain = []
        for section in i.split('.'):
            domain.append(str(section))
        for sect in range(len(domain)):
            try:
                if domain[sect] == 'blogspot':
                    domain = ['blogspot','com']
                    break

                try:
                    if domain[sect][:3] in ['com'] and domain[sect+1][:2] in ['pl']:
                        domain[sect] = 'com'
                        domain[sect+1] = 'pl'
                        domain = domain[:sect+2]
                        break
                except IndexError:
                    pass
                if domain[sect][:2] in ['pl','uk', 'eu'] :
                    domain[sect] = domain[sect][:2]
                    domain = domain[:sect+1]
                elif domain[sect][:3] in ['com','gov']:
                    domain[sect] = domain[sect][:3]
                    domain = domain[:sect+1]
                elif domain[sect][:4] == 'info':
                    domain[sect] = domain[sect][:4]
                    domain = domain[:sect+1]
            except IndexError:
                pass
        i = '.'.join(domain)
        if i not in uzyte:
            w = whois.query(i)
            uzyte.append(i)
            if 'Consulting' in w.registrar:
                print('Znalazłem!               : '),
                print(i)


colide()