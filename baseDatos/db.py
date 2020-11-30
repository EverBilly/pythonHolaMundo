import mysql.connector

midb = mysql.connector.connect(
    host = 'localhost',
    user = 'ever',
    password = 'Ever2020--',
    database = 'prueba_python'
)

cursor = midb.cursor()

cursor.execute('select * from usuario')
resultado = cursor.fetchall()
print(resultado)

# sql = 'insert into usuario(nombre) values (%s)'
# values = ('Jose', )

# cursor.execute(sql, values)
# midb.commit()

# print(cursor.rowcount)
