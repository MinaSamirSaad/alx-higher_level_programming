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
    cur.execute("SELECT c.name FROM cities as c \
            INNER JOIN states as s ON c.state_id = s.id \
            WHERE s.name = '{}' \
            ORDER BY c.id".format(argv[4]))
    print(", ".join([row[0] for row in cur.fetchall()]))
    cur.close()
    conn.close()
