#!/usr/bin/python3
"""
List all states from DB hbtn_0e_4_usa
Arguments:
    username - username to connect the mySQL
    mysql passwd - password to connect the mySQL
    DB name - Name of the database
    state name - Name of the state to search
"""

if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute(
        "SELECT cities.name FROM cities, states\
        where states.id=cities.state_id AND states.name=%s\
        order by cities.id", (argv[4], ))
    rows = cur.fetchall()
    if len(rows) == 0:
        print()
    else:
        for row in rows:
            print(row[0], end=", " if row != rows[-1] else "\n")
    cur.close()
    db.close()
