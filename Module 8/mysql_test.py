"""
Title: mysql_test.py
Author: Zachary Tharp
Date July 19, 2023
Description: A program to test the mysql connection with team and player tables
"""

""" import statements """
import mysql.connector
from mysql.connector import errorcode

""" database config """
config = {
    "user": "pysports_user"
    "password":"TeamsAreGreat7!"
    "host": "127.0.0.1"
    "database": "pysports"
    "raise_on_warnings": "True"
}

try:
    """ try/catch block for handling potential MySQL database errors """
    db = mysql.connector.connect(**config) # connect to pysports database

    # output the connection status
    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

    input("\n\n Press any key to continue...")

expect mysql.connector.Error as err:
""" on error code """

if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("The supplied username or password are invalid")

elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("The specified database does not exist")

else:
    print(err)

finally:
""" close connection to MySQL """

db.close()
