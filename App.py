from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

# initializations
app = Flask(__name__)

# Mysql Connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flaskcrud'
mysql = MySQL(app)

# settings
app.secret_key = "mysecretkey"

# routes
@app.route('/')
def Index():
    return render_template('index.html')


@app.route('/estudiantes')
def estudiantes():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contacts')
    data = cur.fetchall()
    cur.close()
    return render_template('estudiantes.html', contacts = data)


@app.route('/add_contact', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        cc = request.form['cc']
        fullname = request.form['fullname']
        lastname = request.form['lastname']
        phone = request.form['phone']
        email = request.form['email']
        semester = request.form['semester']

    if cc=='' or fullname=='' or lastname=='' or phone=='' or email=='' or semester=='':
        flash('Recuerda Rellenar Todos los Campos')
        return redirect(url_for('estudiantes'))

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO contacts (cc, fullname, lastname, phone, email, semester) VALUES (%s,%s,%s,%s,%s,%s)", (cc, fullname, lastname, phone, email, semester))
    mysql.connection.commit()
    flash('Estudiante Agregado Satisfactoriamente')
    return redirect(url_for('estudiantes'))



@app.route('/edit/<id>', methods = ['POST', 'GET'])
def get_contact(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM contacts WHERE id=%s",(id,))
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('edit-contact.html', contact = data[0])


@app.route('/update/<id>', methods=['POST'])
def update_contact(id):
    if request.method == 'POST':
        cc = request.form['cc']
        fullname = request.form['fullname']
        lastname = request.form['lastname']
        phone = request.form['phone']
        email = request.form['email']
        semester = request.form['semester']
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE contacts
            SET cc = %s,
                fullname = %s,
                lastname = %s,
                email = %s,
                phone = %s,
                semester = %s
            WHERE id = %s
        """, (cc, fullname, lastname, email, phone, semester, id))
        flash('Operacion ¡Exitosa!')
        mysql.connection.commit()
        return redirect(url_for('estudiantes'))



@app.route('/delete/<string:id>', methods = ['POST','GET'])
def delete_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM contacts WHERE id = {0}'.format(id))
    mysql.connection.commit()
    flash('Estudiante Eliminado Satisfactoriamente')
    return redirect(url_for('estudiantes'))



#MANEJO Y ADMINISTRACION DE LOS ESPACIOS ACADEMICOS:
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////

#CON ESTA FUNCION CONSULTAMOS EN LA BASE DE DATOS
#TODOS QUE TENGA NUESTRA TABLA MATERIAS.
@app.route('/materias')
def materias():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM materias')
    data = cur.fetchall()
    cur.close()
    return render_template('materias.html', materias = data)

#LA SIGUIENTE RUTA NOS SIRVE PARA GUARDAR LOS DATOS
#MEDIANTE EL METODO POST DE NUESTRA VISTA MATERIAS.
@app.route('/add_materia', methods=['POST'])
def add_materia():
    if request.method == 'POST':
        nombre = request.form['nombre']
        semestre = request.form['semestre']

    if nombre=='' or semestre=='':
        flash('Recuerda Rellenar Todos los Campos')
        return redirect(url_for('materias'))

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO materias (nombre, semestre) VALUES (%s,%s)", (nombre, semestre))
    mysql.connection.commit()
    flash('Espacio Academico Agregado Satisfactoriamente')
    return redirect(url_for('materias'))

#LA SIGUIENTE FUNCION ME EDITA LOS REGISTROS EN LA TABLA
#MATERIAS MEDIANTE METODOS POST, GET UTILIZANDO EL LLAMDO
#MEDIANTE EL CAMPO ID DE LA TABLA MATERIAS.
@app.route('/editM/<id>', methods = ['POST', 'GET'])
def get_materias(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM materias WHERE id=%s",(id,))
    data = cur.fetchall()
    cur.close()
    #print(data[0])
    return render_template('edit-materias.html', materias = data[0])


@app.route('/updateM/<id>', methods=['POST'])
def update_materias(id):
    if request.method == 'POST':
        nombre = request.form['nombre']
        semestre = request.form['semestre']
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE materias
            SET nombre = %s,
                semestre = %s
            WHERE id = %s
        """, (nombre, semestre, id))
        flash('Operacion ¡Exitosa!')
        mysql.connection.commit()
        return redirect(url_for('materias'))

#LA SIGUIENTE FUNCION NOS PERMITE ELIMINAR DATOS DE
#LA TABLA MATERIAS.
@app.route('/deleteM/<string:id>', methods = ['POST','GET'])
def delete_materias(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM materias WHERE id = {0}'.format(id))
    mysql.connection.commit()
    flash('Espacio Academico Eliminado Satisfactoriamente')
    return redirect(url_for('materias'))




#MANEJO Y ADMINISTRACION DE LOS LAS SESIONES:
#//////////////////////////////////////////////////////////////////////////////////////

@app.route('/reserva')
def reservar():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM sesiones')
    data = cur.fetchall()
    cur.close()
    cur2 = mysql.connection.cursor()
    cur2.execute('SELECT * FROM materias')
    data2 = cur2.fetchall()
    cur2.close()
    return render_template('reserva.html', reserva = data, materias2 = data2)


@app.route('/add_reserva', methods=['POST'])
def add_reserva():
    if request.method == 'POST':
        fecha = request.form['fecha']
        hora_inicio = request.form['hora_inicio']
        hora_fin = request.form['hora_fin']
        id_materia = request.form['id_materia']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO sesiones (fecha,hora_inicio,hora_fin,id_materia) VALUES (%s,%s,%s,%s)", (fecha,hora_inicio,hora_fin,id_materia))
        mysql.connection.commit()
        flash('Sesion Añadida satisfactoriamente')
        return redirect(url_for('reservar'))


@app.route('/ver/<id>', methods = ['POST', 'GET'])
def ver(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM sesiones WHERE id_sesion = %s', (id,))
    data = cur.fetchall()
    cur.close()

    cur2 = mysql.connection.cursor()
    cur2.execute('SELECT * FROM contacts')
    data2 = cur2.fetchall()
    cur2.close()

    cur3 = mysql.connection.cursor()
    cur3.execute('SELECT * FROM materias')
    data3 = cur3.fetchall()
    cur3.close()
    return render_template('ver.html', sesiones = data[0], estudiantes = data2, materias = data3)



@app.route('/delete_sesion/<int:id>/', methods = ['POST','GET'])
def delete_sesion(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM sesiones WHERE id_sesion = {0}'.format(id))
    mysql.connection.commit()
    flash('Sesion Removida')
    return redirect(url_for('reservar'))


@app.route('/edit_sesiones/<id>', methods = ['POST', 'GET'])
def get_sesiones(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM sesiones WHERE id_sesion = %s', (id,))
    data = cur.fetchall()
    cur.close()
    cur3 = mysql.connection.cursor()
    cur3.execute('SELECT * FROM materias')
    data3 = cur3.fetchall()
    cur3.close()
    print(data[0])
    return render_template('edit-sesiones.html', sesion = data[0], materias3 = data3)


@app.route('/update_sesiones/<id>', methods=['POST'])
def update_sesiones(id):
    if request.method == 'POST':
        fecha = request.form['fecha']
        hora_inicio = request.form['hora_inicio']
        hora_fin = request.form['hora_fin']
        id_materia = request.form['id_materia']
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE sesiones
            SET fecha = %s,
                hora_inicio = %s,
                hora_fin = %s,
                id_materia = %s
            WHERE id_sesion = %s
        """, (fecha,hora_inicio,hora_fin,id_materia, id))
        flash('Operacion ¡Exitosa!')
        mysql.connection.commit()
        return redirect(url_for('reservar'))




# starting the app
if __name__ == "__main__":
    app.run(port=3000, debug=True)