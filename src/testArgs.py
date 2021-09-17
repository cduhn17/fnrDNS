#!/usr/bin/python3


"""Usage: testArgs.py

Options:
    -h --help   Show this message
    --version   Show version.


"""

import csv
import socket
import os

from datetime import datetime

# Third party packages
import sublist3r

import dns.resolver

def getDomain():
    myDict = {'google.com': '1.1.1.31','hotmail.com': '1.1.1.2' }
    # with open('../current-full.csv') as csvFile:
    #
    #     csv_reader = csv.reader(csvFile, delimiter=',')
    #     line_count = 0
    #     domainData = {}
    #     for row in csv_reader:
    #         if line_count == 0:
    #             line_count += 1
    #         else:
    #             domaninName = row[0]
    #             # print(f'The domain {row[0]}')
    #             domainData[f'{domaninName}'] = ' '
    #             line_count += 1
    return myDict


def theaddress(address):
    """Get actual FQDN of IP

    """

    theDomainInfo = {}

    gettheAddress = ''


    # thedomain = thedomain

    try:
        thename = (address,80)
        gettheAddress = socket.gethostbyaddr(address)

        # print(gettheAddress)
        # theDomainInfo[f'{address}'] = gettheAddress
    except socket.gaierror:
        print('There is a problem with the Domain that you selected')
        # theDomainInfo[f'{address}'] = 'NULL'


    # print(gettheAddress)

    return gettheAddress




def thename(address):
    """Get actual IP address of domain

    """

    theDomainInfo = {}

    gettheAddress = ''


    # thedomain = thedomain

    try:

        gettheAddress = socket.getaddrinfo(f'{address}', 80, family=socket.AF_INET, proto=socket.IPPROTO_TCP)

        # print(gettheAddress)
        # theDomainInfo[f'{address}'] = gettheAddress
    except socket.gaierror:
        print('There is a problem with the Domain that you selected')
        # theDomainInfo[f'{address}'] = 'NULL'


    print(gettheAddress)

    return gettheAddress

def findSub(domain):
    subdomains = sublist3r.main(domain, 40, 'wvot.txt', ports=None, silent=False, verbose=False, enable_bruteforce=False, engines=None)

    return subdomains





def main():
    todaysDate = datetime.today().strftime('%m/%d/%Y')


    theIP = '129.71.224.67'

    output = os.popen('dig @1.1.1.1 -x 129.71.224.67 +short')

    print(output.read())

    # for x in theaddress('129.71.224.67'):
    #     print(x)


    # print(nt)






if __name__ == '__main__':
    main()
