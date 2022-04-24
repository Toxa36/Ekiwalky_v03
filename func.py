import sqlite3

with sqlite3.connect("cards_regular.db") as wdb:
    cur = wdb.cursor()

def return_base(dice_roll, num):
    with sqlite3.connect("cards_regular.db") as wdb:
        cur = wdb.cursor()
        print('кубик=', dice_roll, ' ID карты=', num)
        cur.execute(f"""SELECT * FROM base WHERE Dice = {dice_roll} 
        AND ID = 8*({dice_roll}-1) + {num} """)
        result = cur.fetchone()
        print('селект прошел', result)
        return result

def return_add(dice_roll, text6):
    with sqlite3.connect("cards_regular.db") as wdb:
        dice_roll = int(dice_roll)
        text6 = text6
        if text6:
            curs = wdb.cursor()
            curs.execute(f"""SELECT * FROM six WHERE ID = {text6}""")
            result = curs.fetchone()
            print('селект 6 прошел', result)
            return result
        else:
            curs = wdb.cursor()
            curs.execute(f"""SELECT * FROM one_five 
                        WHERE Dice = {dice_roll}""")
            result = curs.fetchone()
            print('селект 2 прошел', result)
            return result


def test(name):
    print(name)

#wdb.close()