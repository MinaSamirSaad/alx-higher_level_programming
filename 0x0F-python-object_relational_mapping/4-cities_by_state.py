#!/usr/bin/python3
"""
List all states from DB hbtn_0e_usa
Arguments:
    username - username to connect the mySQL
    mysql passwd - password to connect the mySQL
    DB name - Name of the database
"""

if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute(
        "SELECT cities.id, cities.name, states.name FROM cities, states\
        where states.id=cities.state_id order by cities.id")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
