import sqlite3

with sqlite3.connect('blog.db') as conn:
    c = conn.cursor()

    '''
    #c.execute("DROP TABLE posts")
    c.execute("""CREATE TABLE posts (title TEXT, post TEXT)""")

    c.execute('INSERT INTO posts VALUES ("Good", "I\'m good.")')
    c.execute('INSERT INTO posts VALUES ("Well", "I\'m well.")')
    c.execute('INSERT INTO posts VALUES ("Excellent", "I\'m excellent.")')
    c.execute('INSERT INTO posts VALUES ("Okay", "I\'m okay.")')
    '''

    c.execute("SELECT * from posts")
    rows = c.fetchall()

    for r in rows:
        print r[0], r[1]
