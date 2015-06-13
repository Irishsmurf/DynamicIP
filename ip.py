import os
import boto.route53 as aws
import json
import urllib
from netifaces import interfaces, ifaddresses, AF_INET

URL = 'http://ip.paddez.com/?json'
response = urllib.urlopen(URL)

data = json.loads(response.read())

REGION = 'eu-west-1'
DOMAIN = 'paddez.ninja'
OSLO = 'oslo.paddez.ninja'
RIGA = 'riga.paddez.ninja'

ZONE_ID = 'ZV26VXQ9WNYSB'

IP = data.get('ip')

r53 = aws.connect_to_region(REGION)
zone = r53.get_zone(DOMAIN)
apex = zone.get_a(DOMAIN)
oslo = zone.get_a(OSLO)
print oslo
addrs = ifaddresses('eth0')[AF_INET]
private_ip = addrs[0].get('addr')


if(IP != apex.to_print()):
	print zone.update_a(DOMAIN, IP)

if(private_ip != oslo.to_print()):
	print zone.update_a(OSLO, private_ip)


