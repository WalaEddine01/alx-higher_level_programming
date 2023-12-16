#!/usr/bin/python3
"""
this Module lists the states that matches with the user input
"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    conn = MySQLdb.connect(
        host="localhost",
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        port=3306
    )
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name like BINARY\
                '{}' ORDER BY states.id ASC".format(argv[4]))

    for row in cur:
        print(row)
    cur.close()
    conn.close()
