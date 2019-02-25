#!/usr/bin/python3

from print_msg import print_msg
import mysql.connector
from mysql.connector import errorcode
import time

def main():

    user_name = input('Enter usename: ')
    db_name = input('Enter database name: ')

    start_time = time.time()

    try:
        db_conn = mysql.connector.connect(
            user=user_name,
            host='127.0.0.1',
            database=db_name,
            unix_socket='/var/run/mysqld/mysqld.sock',
        )
        cursor = db_conn.cursor()
        print_msg('status', 'Connecting...')
        if db_conn.is_connected():
            print_msg('ok', 'Succesfully connected!')

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print_msg('error', 'Wrong user name or password')
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print_msg('error', 'Database does not exists!')
        else:
            print_msg('error', 'An error has occured!')

    print_msg('time', f'{round(time.time() - start_time, 4)} s')

if __name__ == '__main__':
    main()
