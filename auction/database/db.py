# xata database connection 

import psycopg2


def connection_init():
    cnn = psycopg2.connect(
    dbname="cricket-auction:main",
    user="6grupu",
    password="xau_Y0NNvDfnc6K9LILYo1qBqtqpunqV2kyi0",
    host="us-east-1.sql.xata.sh",
    port=5432,
    )
    return cnn
# cur = cnn.cursor()
# cur.execute("SELECT 1")
# print(cur.fetchone())
# cnn.close()

def connection_test():
    cnn = connection_init()
    cur = cnn.cursor()
    cur.execute("SELECT 1")
    print(cur.fetchone())
    cnn.close()