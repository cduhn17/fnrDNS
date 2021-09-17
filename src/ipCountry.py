#!/usr/bin/python3


import re
import json
import urllib.request

def getMyLocation(address):
    url = f'http://ipinfo.io/{address}'
    response = urllib.request.urlopen(url)
    data = json.load(response)

    IP = data['ip']
    org = data['org']
    city = data['city']
    country = data['country']
    region = data['region']

    print('Your IP detail\n ')
    if country == 'US':
        print(f"IP : {IP} \nRegion : {region} \nCountry : {country} \nCity : {city} \nOrg : {org}")
    else:
        print(f"The address was not from the US it was from {country}")






def main():
    getMyLocation('67.22.200.92')
    getMyLocation('192.206.151.131')


if __name__ == '__main__':
    main()
