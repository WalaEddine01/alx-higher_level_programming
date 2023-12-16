#!/usr/bin/python3
""" Module that contains a script that lists all states from the database
    hbtn_0e_0_usa.
"""
if __name__ == "__main__":
    import MySQLdb
    import sys

    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    con = MySQLdb.connect(host="localhost", user=user,
                          passwd=password,
                          db=db_name,
                          port=3306)
    cur = con.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    for row in cur.fetchall():
        print(row)
    cur.close()
    con.close()
