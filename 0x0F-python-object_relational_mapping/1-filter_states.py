#!/usr/bin/python3
""" lists all states with a name starting with
    N (upper N) from the database hbtn_0e_0_usa"""

import MySQLdb
import sys
"""importing MySQLdb and sys module"""

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', user=sys.argv[1], port=3306,
                         passwd=sys.argv[2], db=sys.argv[3], charset='utf8')
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE
                'N%' ORDER BY states.id ASC")
    states1 = cur.fetchall()
    for state in states1:
        print(state)
