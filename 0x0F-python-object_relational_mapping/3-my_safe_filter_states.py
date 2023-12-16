#!/usr/bin/python3
"""
This module contains script that protect from the SQL Injection...
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
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY\
                %s ORDER BY states.id ASC", (state_name,))

    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()
