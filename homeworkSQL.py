import sqlite3

kit = ['элемент', 22, 'списка', 10, 'слово', 33]


if __name__ == '__main__':

    db = sqlite3.connect("domBase.db")
    courser = db.cursor()

    courser.execute('''
    CREATE TABLE IF NOT EXISTS textTabl
    (id INTEGER PRIMARY KEY AUTOINCREMENT,
    texts TEXT);
    ''')
    db.commit()

    courser.execute('''
    CREATE TABLE IF NOT EXISTS numTabl
    (id INTEGER PRIMARY KEY AUTOINCREMENT,
    number INTEGER);
    ''')
    db.commit()

    for cell in kit:
        if type(cell) is str:
            courser.execute('''INSERT INTO textTabl(texts) VALUES (?);''', (cell,))
            db.commit()
            num = int(len(cell))
            courser.execute('''INSERT INTO numTabl(number) VALUES (?);''', (num,))
            db.commit()
        elif type(cell) is int:
            if cell % 2 == 0:
                courser.execute('''INSERT INTO numTabl(number) VALUES (?);''', (cell,))
                db.commit()
            else:
                courser.execute('''INSERT INTO textTabl(texts) VALUES ('нечетное');''')
                db.commit()

    courser.execute('''SELECT Count(*) FROM numTabl''')
    id = courser.fetchall()

    if int(id[0][0]) > 5:
        courser.execute('''DELETE FROM textTabl WHERE id=1;''')
        db.commit()
    else:
        courser.execute('''UPDATE textTabl SET texts = 'hello' WHERE id = 1''')
        db.commit()
        
    courser.close()
