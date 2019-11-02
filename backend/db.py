import mysql.connector
from mysql.connector import errorcode

DB_CONFIG = {
    'user':'root',
    'password':'pass',
    'database':'classicmodels',
    'host':'127.0.0.1',
    'auth_plugin':'mysql_native_password'
}
def getDBConn():
    try:
        cnx = mysql.connector.connect(**DB_CONFIG)
        return cnx
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Access denied")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        return null
