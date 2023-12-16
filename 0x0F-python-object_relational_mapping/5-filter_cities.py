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
    state_name = argv[4]

    conn = MySQLdb.connect(
        host="localhost",
        user=user,
        passwd=password,
        db=db_name,
        port=3306
    )
    cur = conn.cursor()
    cur.execute("SELECT name FROM cities WHERE state_id = \
                (SELECT id FROM states WHERE name LIKE BINARY %s)\
                ORDER BY cities.id ASC", (state_name,))

    t = ()
    for row in cur:
        t += row
    print(*t, sep=", ")

    cur.close()
    conn.close()
