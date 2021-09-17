#!/usr/bin/python3


"""This module contains the pastgresql dbconfig.config code."""

from configparser import ConfigParser

databaseConfig = '/Users/duhnc/Desktop/allInfo/whoIS/src/dbconfig.config'



def config(filename=databaseConfig, section='postgresql'):

    """Reads .config file that contains DB credentialsv gy7

    """

    parser = ConfigParser()

    parser.read(filename, encoding='utf-8')

    db = {}

    if parser.has_section(section):
        params = parser.items(section)

        for param in params:
            db[param[0]] = param[1]

    else:
        raise Exception(f'Section {section} not found in {filename}')

    return db

