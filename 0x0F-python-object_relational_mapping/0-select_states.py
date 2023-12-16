#!/usr/bin/python3
""" Module that contains a script that lists all states from the database
    hbtn_0e_0_usa.
"""
if __name__ == "__main__":
    import MySQLdb
    con = MySQLdb.connect(host="localhost", user="root", passwd="123", db="hbtn_0e_0_usa", port=3306)
    cur = con.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    for row in cur.fetchall():
        print(row)
    cur.close()
    con.close()