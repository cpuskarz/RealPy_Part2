import sqlite3

with sqlite3.connect('cars.db') as conn:
    c = conn.cursor()
    """
    c.execute("INSERT INTO inventory VALUES('Ford', 'Taurus', 5)")
    c.execute("INSERT INTO inventory VALUES('Ford', 'Pinto', 3)")
    c.execute("INSERT INTO inventory VALUES('Ford', 'Explorer', 15)")
    c.execute("INSERT INTO inventory VALUES('Honda', 'Accord', 54)")
    c.execute("INSERT INTO inventory VALUES('Honda', 'Civic', 1)")


    c.execute("UPDATE inventory SET quantity = 7 WHERE model='Pinto'")
    c.execute("UPDATE inventory SET quantity = 17 WHERE model='Explorer'")
    """

    c.execute("SELECT * FROM inventory WHERE make='Ford'")
    rows = c.fetchall()

    for r in rows:
        print r[0], r[1], r[2]

