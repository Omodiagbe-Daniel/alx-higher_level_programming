#!/usr/bin/python3

""" a script that lists all cities from the database hbtn_0e_4_usa """

import MySQLdb
from sys import argv

if __name__ == "__main__":
    count = 0
    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset='utf8')

    cur = db.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name FROM cities
                LEFT JOIN states ON states.id = cities.state_id
                WHERE states.name LIKE %s
                ORDER BY cities.id""", (argv[4],))
    cities = cur.fetchall()
    for city in cities:
        if city[2] == argv[4]:
            if count > 0:
                print(", ", end='')
        print(city[1], end='')
        count += 1
    print()
