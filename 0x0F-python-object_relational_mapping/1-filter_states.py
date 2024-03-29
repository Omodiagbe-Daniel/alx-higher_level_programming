#!/usr/bin/python3
"""a script that lists all states with a name starting
    with N (upper N) from the database hbtn_0e_0_usa """

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', user=sys.argv[1], port=3306,
                         passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = db.cursor()
    cur.execute("""SELECT * FROM states WHERE name LIKE
                'N%' ORDER BY states.id ASC""")
    states1 = cur.fetchall()
    if states1 is not None:
        for state in states1:
            if state[1][0] == 'N':
                print(state)
