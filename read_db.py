import sqlite3


def print_data_2d(column_names, data):
    print(column_names)
    for line in data:
        print(line)
    print('number of lines in database table is ' +str(len(data)))



def sqlite_read_db(data_base, table, column_name = None):
    """
    функция чтения всех данных из базы данных
    """
    con = sqlite3.connect(data_base)
    cur = con.cursor()
    query_columns = 'PRAGMA table_info('+table+')'
    cur.execute(query_columns)
    column_descriptions = cur.fetchall() # fetcone() - считывает одну запись
    column_names = []
    for column in column_descriptions:
        column_names.append(column[1])

    if column_name is None:
        query = 'SELECT * FROM ' + table
        cur.execute(query)
        data = cur.fetchall() # Помещаем считанные записи из запроса в переменную data
    else:
        query = 'SELECT '+column_name+' FROM ' + table
        cur.execute(query)
        data = cur.fetchall()
        new_data =[]
        for el in data:
            new_data.append(el[0])
        data = new_data
        del(new_data)

    cur.close()
    con.close()
    return print_data_2d(column_names, data)




if __name__ =='__main__':
    data_base = 'example.db'
    table = 'city'
    # column_name = ''
    sqlite_read_db(data_base, table)
