import os
import boto.route53 as aws
import json
import urllib

URL = 'http://ip.paddez.com/?json'
response = urllib.urlopen(URL)

data = json.loads(response.read())

REGION = 'eu-west-1'
DOMAIN = 'paddez.ninja'
ZONE_ID = 'ZV26VXQ9WNYSB'

IP = data.get('ip')

r53 = aws.connect_to_region(REGION)
zone = r53.get_zone(DOMAIN)
apex = zone.get_a(DOMAIN)

if(IP != apex.to_print()):
	print zone.update_a(DOMAIN, IP)


