#!/usr/bin/python3


import socket

import os

import asyncio

import psycopg2

import psycopg2.extras

import logging

from time import time

from datetime import datetime

import csv

import json

import urllib.request

from multiprocessing import Process

#Import from local module 'config'
from config import config

# Third party packages
import sublist3r
from reverseip import *

conn = None
cursor = None

todaysDate = datetime.today().strftime('%m/%d/%Y')


logging.basicConfig(filename='../logs/whoisLog.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S', level=logging.INFO)

def findSub():
    subdomains = sublist3r.main('wvot.gov', 40, 'wvot.txt', ports=None, silent=False, verbose=False, enable_bruteforce=False, engines=None)



def setAllDomains(hostname):
    """Insert domain into the database.

    """
    # logging.info(f"Started setAllDomains {hostname}")
    global conn, cursor
    try:
        logging.info('Got here in setAllDomains')

        params = config()

        conn = psycopg2.connect(**params)


        if conn:

            logging.info(f'There was a connection made to the database and the query was executed ')

            cursor = conn.cursor()

            cursor.execute(f"insert into domain_assets(domain_name) values('{hostname}');")




    except (Exception, psycopg2.DatabaseError) as err:
        logging.error(f'There was a problem logging into the psycopg database {err}')
    finally:
        if conn is not None:
            conn.commit()
            cursor.close()
            conn.close()
            logging.info('The connection/query was completed and closed.')

def setDomainIP(hostname, ipaddress):
    """Update database table with IP address that came back from reverse domain lookup

    """
    global conn, cursor
    try:
        logging.info('Got here.')

        params = config()

        conn = psycopg2.connect(**params)

        # query = f"""INSERT INTO {}<table_name>(<col1>,<col2>) values(<val1>,<val2>)"""


        if conn:
            logging.info(f'There was a connection made to the database and the query was executed ')

            cursor = conn.cursor()

            cursor.execute(f"update domain_assets set domain_ip='{ipaddress}', date_saved='{todaysDate}', last_day_changed='{todaysDate}' where domain_name = '{hostname}'")


    except (Exception, psycopg2.DatabaseError) as err:
        logging.info(f'There was a problem logging into the psycopg database {err}')
    finally:
        if conn is not None:
            conn.commit()
            cursor.close()
            conn.close()
            logging.info('The connection/query was completed and closed.')

def updateDomainIP(hostname, ipaddress):
    """Update database table with IP address that came back from reverse domain lookup

    """
    global conn, cursor
    try:
        logging.info('Got here.')

        params = config()

        conn = psycopg2.connect(**params)

        # query = f"""INSERT INTO {}<table_name>(<col1>,<col2>) values(<val1>,<val2>)"""


        if conn:
            logging.info(f'There was a connection made to the database and the query was executed ')

            cursor = conn.cursor()

            cursor.execute(f"update domain_assets set domain_ip='{ipaddress}', last_day_changed='{todaysDate}' where domain_name = '{hostname}'")


    except (Exception, psycopg2.DatabaseError) as err:
        logging.info(f'There was a problem logging into the psycopg database {err}')
    finally:
        if conn is not None:
            conn.commit()
            cursor.close()
            conn.close()
            logging.info('The connection/query was completed and closed.')


def getDomain():
    """Isolate all domain from CSV file. Returns dict of all domain. Also return if there were any new domain.

    """
    domainData = {}
    newDomains = {}
    updatedDomains = {}
    test = 1
    if test == 0:
        with open('/Users/duhnc/Desktop/allInfo/whoIS/current-full.csv') as csvFile:

            csv_reader = csv.reader(csvFile, delimiter=',')
            line_count = 0

            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                else:
                    domaninName = row[0]
                    # print(f'The domain {row[0]}')
                    domainData[f'{domaninName}'] = 'NULL'
                    line_count += 1
            # print(domainData)
            for theDomain in domainData.items():

                domainName = theDomain[0]
                domainAddress = theaddress(domainName)
                if getCountry(domainAddress) == "US":
                    currentDomains = getAllDomainInfo()
                    # print(f'this is the domain {domainName}')
                    if domainName not in currentDomains:
                        logging.info('We found a MISSING domain.')
                        setAllDomains(theDomain[0])
                        newDomains[f'{domainName}'] = 'NULL'
                        setDomainIP(domainName, domainAddress)
                        print(domainAddress)

                    else:
                        logging.info('We found a domain. Nothing was inserted.')
                        ipfromDBcurrentDomainname = currentDomains.get(domainName)
                        if ipfromDBcurrentDomainname == domainAddress:
                            pass
                        else:
                            updateDomainIP(domainName, domainAddress)
                            updatedDomains[f'{domainName}'] = domainAddress

                        return newDomains, updatedDomains
    else:
        with open('/Users/duhnc/Desktop/allInfo/whoIS/test-full.csv') as csvFile:

            csv_reader = csv.reader(csvFile, delimiter=',')
            line_count = 0
            domainData = {}
            newDomains = {}
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                else:
                    domaninName = row[0]
                    # print(f'The domain {row[0]}')
                    domainData[f'{domaninName}'] = 'NULL'
                    line_count += 1
            # print(domainData)
            for theDomain in domainData.items():

                domainName = theDomain[0]
                print(domainName)
                domainAddress = theaddress(domainName)
                if getCountry(domainAddress) == "US":
                    print(getCountry(domainAddress))
                #     currentDomains = getAllDomainInfo()
                #     # print(f'this is the domain {domainName}')
                #     if domainName not in currentDomains:
                #         logging.info('We found a MISSING domain.')
                #         setAllDomains(theDomain[0])
                #         newDomains[f'{domainName}'] = 'NULL'
                #         # print(domainAddress)
                #         setDomainIP(domainName, domainAddress)
                #
                #     else:
                #         logging.info('We found a domain. Nothing was inserted.')
                #         ipfromDBcurrentDomainname = currentDomains.get(domainName)
                #         if ipfromDBcurrentDomainname == domainAddress:
                #             pass
                #         else:
                #             updateDomainIP(domainName, domainAddress)
                #             updatedDomains[f'{domainName}'] = domainAddress
                #
                #         return newDomains, updatedDomains
                # else:
                #     print('No IP from the US were found')



def getAllDomainInfo():
    """Make database pull to get available domain name and IP address.

    """

    global conn, cursor
    resultDict = {}
    try:
        # logging.info('Got here in getAll DomainInfo')

        params = config()

        conn = psycopg2.connect(**params)


        if conn:
            logging.info(f'There was a connection made to the database and the query was executed ')

            cursor = conn.cursor(cursor_factory = psycopg2.extras.DictCursor)

            cursor.execute(f"select domain_name, domain_ip from domain_assets;")



            result = cursor.fetchall()



            for row in result:

                theDomain = row[0]
                theIP = row[1]

                resultDict[f'{theDomain}'] = f'{theIP}'
            return resultDict
                # if theIP == 'NULL':
                #     theaddress(theDomain)




    except (Exception, psycopg2.DatabaseError) as err:
        logging.error(f'There was a problem logging into the psycopg database {err}')
    finally:
        if conn is not None:

            cursor.close()
            conn.close()
            logging.info('The connection/query was completed and closed.')

            return resultDict

def getCountry(address):
    url = f'http://ipinfo.io/{address}'
    response = urllib.request.urlopen(url)
    data = json.load(response)

    IP = data['ip']
    org = data['org']
    city = data['city']
    country = data['country']
    region = data['region']

    # print('Your IP detail\n ')
    # if country == 'US':
    #     print(f"IP : {IP} \nRegion : {region} \nCountry : {country} \nCity : {city} \nOrg : {org}")
    return country



def theaddress(address):
    """Get actual IP address of domain

    """

    theDomainInfo = {}

    gettheAddress = ''





    # thedomain = thedomain

    try:

        gettheAddress = socket.gethostbyname(f'{address}')
        setDomainIP(address, gettheAddress)
        # print(gettheAddress)
        # theDomainInfo[f'{address}'] = gettheAddress
    except socket.gaierror:
        print('There is a problem with the Domain that you selected')
        # theDomainInfo[f'{address}'] = 'NULL'


    print(gettheAddress)

    return gettheAddress

def reverseIPStuff(address):
    apikey = os.environ.get('WHOIS_VAR')
    client = Client(apikey)
    allDomains = {}

    result = client.data(address)
    # print(result.size)
    for record in result.result:

        # record = str(record.name)
        allDomains[record.name] = address

    return allDomains


def main():
    # allDomains = getDomain()


    start_time = datetime.now()


    # allDomains = getDomain()

    print(f"The time as started at {start_time.strftime('%I:%M:%S')}...")




    # TODO get lenght of allNewDomains and if GT 0 then take allNewDomains and get them into the database with an IP
    # TODO find where existing domains are saved and when ip is saved
    # TODO find when new domains are saved and ip saved

    # allNewDomains = getDomain()
    getDomain()



    # await asyncio.gather(getDomain())

    # TODO pass the function theaddress into getDomain() and process the information and determine what domains have changed or not





    end_time = datetime.now()
    total_time = end_time - start_time
    print(f'The total time was {total_time}')
    #
    # print(f'The time that it took to run the proam{time() - start_time}')


if __name__ == '__main__':

    main()

    # asyncio.run(main())
