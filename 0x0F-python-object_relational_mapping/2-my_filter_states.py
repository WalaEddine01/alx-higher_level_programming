#!/usr/bin/python3
"""
this Module lists the states that matches with the user input
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
                '{}' ORDER BY states.id ASC".format(state_name))

    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()
