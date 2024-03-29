from sqlalchemy import create_engine, text
sql_engine = create_engine('POSTGRESQL_URL', pool_pre_ping=True)

def db_record(table_name, msg_dict):
    values = {'time_stamp':datetime.now(),
              'key1':msg_dict['key1'],
              'key2':msg_dict['key2'],
              'key3':json.dumps(msg_dict['key3'])}

    sql = 'insert into ' + table_name
    sql += '''(time_stamp, key1, key2, key3)
              values (:time_stamp, :key1, :key2, :key3)'''
    res = sql_engine.execute(text(sql), **values)

msg_dict={'key1':'xxx',
          'key2':'yyy',
          'key3':{'k1':123,
                  'k2':456},
         }
db_record('myTable',msg_dict)

def db_select(table_name,key1,key2):
    values = {"key1":key1, "key2":key2}
    sql = """select *
                from table_name
                where key1 = :key1 AND key2 = :key2
            """
    res = sql_engine.execute(text(sql), **values)
    for row in res:
        print(row)    # list
db_select('myTable','key1','key2')



