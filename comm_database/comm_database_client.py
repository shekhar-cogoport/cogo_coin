import psycopg2
from config.env import *

def temp():
    conn = psycopg2.connect(database=NAME,
                        host=HOST,
                        user=USERNAME,
                        password=PASSWORD,
                        port=PORT)
    print('connection psycopg2',conn)

    # connection psycopg2 <connection object at 0x1099ed7e0; dsn: 'user=apollo password=xxx dbname=cogoport_api_comm host=login-apollo.dev.cogoport.io port=6432', closed: 0>
    return conn
