#!/usr/bin/python
import subprocess

print "Hello, world"

cmd = "curl \"https://api.keen.io/3.0/projects/556970bbc2266c068405579f/events/purchases?api_key=a07c1589a20e5b4d8ab25aa53d04348dd91292608dbdb2f6cbe8a433fcc42d1f7427b3b7828fa3fb0d363061c5349ebeb3e58bf36125f6609fd12db258c81556078e077b8397abf2da264903e5a7ae76bde38091ea0ca3407118791f146a026d525a27cfbfdc2d9d4fe1e8c8c8d0726b\" -H \"Content-Type: application/json\" -d @purchase1.json"

p = subprocess.Popen(cmd, shell=True)

#p = subprocess.Popen('curl "https://api.keen.io/3.0/projects/556970bbc2266c068405579f/events/purchases?api_key=a07c1589a20e5b4d8ab25aa53d04348dd91292608dbdb2f6cbe8a433fcc42d1f7427b3b7828fa3fb0d363061c5349ebeb3e58bf36125f6609fd12db258c81556078e077b8397abf2da264903e5a7ae76bde38091ea0ca3407118791f146a026d525a27cfbfdc2d9d4fe1e8c8c8d0726b" -H "Content-Type: application/json" -d @purchase1.json')

