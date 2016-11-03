import sqlite3

with sqlite3.connect('new.db') as conn:
    c = conn.cursor()

    c.execute("""SELECT DISTINCT population.city, population.population,
            regions.region FROM population, regions WHERE
            population.city = regions.city ORDER by population.city ASC""")

    rows = c.fetchall()

    for r in rows:
        print "City: {}".format(r[0])
        print "Population: {}".format(str(r[1]))
        print "Region: {}".format(r[2])
        print