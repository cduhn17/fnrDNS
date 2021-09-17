#!/usr/bin/python3

"""

"""

import os

import psycopg2

import logging

from src.config import config

from reverseip import *

from dns import resolver

from dns import reversename



try:
    from urllib.request import urlopen
except ImportError:
    from urllib3 import urlopen

logging.basicConfig(filename='logs/whoisLog.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S', level=logging.INFO)

# whoisAPIKey = os.environ.get('WHOIS_VAR')

# print(f'The key is {WHOIS_VAR}')

def getSomeData():
    global conn, cursor
    try:

        params = config()

        conn = psycopg2.connect(**params)


        if conn:
            logging.info(f'There was a connection made to the database and the query was executed ')

            cursor = conn.cursor()

            cursor.execute(f'select * from thenewdata')

            results = cursor.fetchall()

            for x in results:

                fname = x[1]
                print(f'{fname}')
    except Exception as err:
        logging.info(f'There was a problem logging into the psycopg database {err}')
    finally:
        if conn is not None:
            conn.close()
            logging.info('The connection/query was completed and closed.')
        # cursor.close()
        # conn.commit()
        # conn.close()






def getInfo():
    """ Performs the whois lookup

    """
    domain = "129.71.224.67"



    apikey = os.environ.get('WHOIS_VAR')

    url = f'https://www.whoisxmlapi.com/whoisserver/WhoisService?domainName={domain}&apiKey={apikey}&outputFormat=JSON'

    print(urlopen(url).read().decode('utf8'))

    # client = Client(api_key=f'{whoisAPIKey}')

    # params = RequestParameters(ignore_raw_texts=1, da=2)

    # whois = client.data('whoisxmlapi.com', params)
    # print(whois.domain_availability_raw)

    # # Also you can modify default values of parameters:
    # client.parameters.output_format = 'xml'
    # print(client.raw_data('whoisxmlapi.com'))

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
        # allDomains.append(record.name)
        # print("Domain: {}, visited: {}".format(
        #     record.name, record.last_visit))

    # Get raw API response
    # resp_str = client.raw_data('1.1.1.1')

def iptry(address):

    allNames = {}

    address = reversename.from_address(address)

    nt = resolver.resolve(address,"PTR")


    for x in nt:
        print(x)

    # return nt









def main():
    print(reverseIPStuff('129.71.224.67').keys())
    # getInfo()
    # getSomeData()
    # iptry('129.71.224.67')

if __name__ == '__main__':
    main()