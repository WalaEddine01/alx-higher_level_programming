#!/usr/bin/python3
""" Module that lists all states with a name starting with N (upper N)
    from the database hbtn_0e_0_usa
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
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%'\
                ORDER BY id ASC")
    for row in cur:
        print(row)
    cur.close()
    conn.close()
