#!/usr/bin/python3
"""
This module contains script that lists all cities from
the database hbtn_0e_4_usa
"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    user = argv[1]
    password = argv[2]
    db_name = argv[3]

    conn = MySQLdb.connect(
        host="localhost",
        user=user,
        passwd=password,
        db=db_name,
        port=3306
    )

    cur = conn.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities\
                JOIN states ON cities.state_id = states.id\
                ORDER BY cities.id ASC")

    for row in cur:
        print(row)
    cur.close()
    conn.close()
