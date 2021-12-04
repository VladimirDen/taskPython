import sqlite3
import random

if __name__ == '__main__':
    db = sqlite3.connect("newBase2.db")
    courser = db.cursor()

    courser.execute('''
            CREATE TABLE IF NOT EXISTS adress
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
            indexx INT,
            ndom INT)
            ''')

    courser.execute('''
            INSERT INTO adress(indexx, ndom)
            VALUES (?, ?)''', (random.randint(0, 9), random.randint(0, 9)))

    db.commit()
    courser.execute('''SELECT indexx, ndom FROM adress''')
    a = courser.fetchall()
    print(a)

    if sum(list(map(lambda x: sum(x), a)))/len(a) > len(a):
        courser.execute('''DELETE FROM adress WHERE id = 4 ''')

    courser.execute('''SELECT indexx, ndom FROM adress''')
    a = courser.fetchall()
    print(a)

