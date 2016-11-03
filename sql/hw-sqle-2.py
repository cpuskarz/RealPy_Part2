import sqlite3

with sqlite3.connect('cars.db') as conn:
    c = conn.cursor()

    sql = {
        'Focus count': "SELECT count(make) FROM orders WHERE model = 'Focus'",
        'Civic count': "SELECT count(make) FROM orders WHERE model = 'Civic'",
        'Ranger count': "SELECT count(make) FROM orders WHERE model = 'Ranger'",
        'Accord count': "SELECT count(make) FROM orders WHERE model = 'Accord'",
        'Avenger count': "SELECT count(make) FROM orders WHERE model = 'Avenger'"
    }

    for k, v in sql.iteritems():
        c.execute(v)
        result = c.fetchone()
        print k + ":", result[0]


        