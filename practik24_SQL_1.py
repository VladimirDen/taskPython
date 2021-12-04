import sqlite3

if __name__ == '__main__':
    db = sqlite3.connect("newBase.db")
    courser = db.cursor()
    courser.execute('''
    CREATE TABLE IF NOT EXISTS newbase
    (ID INTEGER PRIMARY KEY AUTOINCREMENT,
    tel INTEGER,
    names TEXT,
    email TEXT)
    ''')

    courser.execute('''
    INSERT INTO newbase(tel, names, email)
    VALUES (?, "ПРИВЕТ", "DASDAS")''', (3,))

    courser.execute('''SELECT * FROM newbase''')
    rows = courser.fetchall()

    for i in rows:
        print(i)
