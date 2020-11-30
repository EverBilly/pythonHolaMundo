from flask import Flask, request, url_for, redirect, abort, render_template
import mysql.connector
#Esta variable obtiene el valor de main
app = Flask(__name__)

midb = mysql.connector.connect(
    host = 'localhost',
    user = 'ever',
    password = 'Ever2020--',
    database = 'prueba_python'
)

# Se manda a la vista por Indice xq son tuplas
# cursor = midb.cursor()
# Se manda a la vista por nombre del encabezado xq es diccionario
cursor = midb.cursor(dictionary=True)

#Decoradores empiezan con @
@app.route('/')
def index():
    return 'BIENVENIDO A LA RAIZ'

# @app.route('/hello/<nombre>', methods=['GET'])
@app.route('/hello/<nombre>', methods=['GET', 'POST'])
def hello(nombre):
    if request.method == 'GET':
        return 'RUTA HELLO GET ' + nombre
    else:
        return 'RUTA HELLO POST ' + nombre

# @app.route('/hello/<nombre>', methods=['POST'])
# def helloPost(nombre):
#     return 'RUTA HELLO POST ' + nombre
@app.route('/formulario', methods=['POST'])
def formulario():
    print(request.form)
    print(request.form['llave1'])
    print(request.form['llave2'])
    return 'Formulario'

# Construyendo URL
@app.route('/url', methods=['POST'])
def url():
    print(url_for('hello', nombre='Ever'))
    return 'URL' 

#Redireccionando Rutas
@app.route('/redireccionar', methods=['GET', 'POST'])
def red():
    # abort(401)
    # abort(403)
    return redirect(url_for('hello', nombre='Ever 2'))

#Renderizando Plantillas
@app.route('/renderizar', methods=['GET', 'POST'])
def renderizar():
    cursor.execute('select * from usuario')
    usuarios = cursor.fetchall()
    # print(usuarios)
    # return render_template('hola.html')
    #Respondiendo con Json
    # return {
    #     'nombre': 'Ever',
    #     'apellido': 'Cifuentes'
    # }
    return render_template('usuarios.html', usuarios = usuarios)
    
# Extendiendo Plantillas
@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html', mensaje='PYTHON')
 
@app.route('/crear', methods=['GET', 'POST'])
def crear():
    if request.method == 'POST':
        nombre = request.form['nombre']
        sql = 'insert into usuario(nombre) values (%s)'
        values = (nombre,)
        cursor.execute(sql, values)
        midb.commit()
        return redirect('renderizar')
    return render_template('crear.html')