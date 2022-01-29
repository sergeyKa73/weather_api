import sqlite3
from get_weather import dict_my

#функция создания db и записи в нее данных
def sqlite_create_db():
    # соединяемся c базой данных
    con = sqlite3.connect('example.db')
    # создаем объект курсора
    cur = con.cursor()
    #создаем таблицу если не существует  добавить id и дату
    cur.execute('CREATE TABLE IF NOT EXISTS city (country TEXT, '
                'city TEXT,'
                't FLOAT,'
                'wind_speed FLOAT,'
                'weather TEXT)')
    #добавляем данные в таблицу
    data = dict_my
    city_data = []
    for val in data.values():
        city_data.append(val)

    cur.execute('INSERT INTO city VALUES(?, ?, ?, ?, ?)', city_data)

    #Записываем данные в таблицу
    con.commit()

    cur.close() # Удаляем курсор
    con.close() # Разрываем соединение

if __name__ =='__main__':
    sqlite_create_db()
