#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    userName = argv[1]
    password = argv[2]
    dbName = argv[3]

    conn = MySQLdb.connect(host="localhost", port=3306, user=userName,
                           passwd=password, db=dbName, charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE BINARY name = '{}' \
            ORDER BY id".format(argv[4]))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
