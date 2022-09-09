#!/usr/bin/python3
"""lists all states from the database hbtn_0e_0_usa:
    Your script should take 3 arguments: mysql username
    mysql password and database name (no argument validation needed).
    You must use the module MySQLdb (import MySQLdb)
    Your script should connect to a
    MySQL server running on localhost at port 3306
    Results must be sorted in ascending order by states.id
    Your code should not be executed when imported."""

import MySQLdb
"""importing MySQLdb"""

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', port=3306, user='root',
                         passwd='Nosetale_1', db='hbtn_0e_0_usa')
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id")
    states1 = cur.fetchall()
    if states1 is not None:
        for state in states1:
            print(state)
        cur.close()
        db.close()
