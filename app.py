<<<<<<< HEAD
from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from models.models import Usuario
from models.modelsp import Producto  # Verifica que este sea el archivo correcto
=======
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from models.models import Usuario
from models.modelsp import Producto
from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
>>>>>>> d37ce8f (TR)
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length
from Conexion.conexion import obtener_conexion

<<<<<<< HEAD
app = Flask(__name__)
app.config['SECRET_KEY'] = 'mi_secreto_seguro'  # Necesario para formularios con CSRF

# Configuración de Flask-Login
=======
app = Flask(__name__)  # Se corrigió '_name_' a '__name__'
app.config['SECRET_KEY'] = 'mi_secreto_seguro'  # Necesario para formularios con CSRF

# Login manager
>>>>>>> d37ce8f (TR)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Definir la clase de formulario
class NombreForm(FlaskForm):
    nombre = StringField('Ingresa tu nombre', validators=[DataRequired(), Length(min=2, max=50)])
    submit = SubmitField('Enviar')

<<<<<<< HEAD
# Ruta principal
=======
# Ruta principal (Página de inicio)
>>>>>>> d37ce8f (TR)
@app.route('/')
def index():
    return render_template('index.html')

<<<<<<< HEAD
# Ruta para formulario con sesión
=======
# Ruta para el formulario
>>>>>>> d37ce8f (TR)
@app.route('/formulario', methods=['GET', 'POST'])
def formulario():
    form = NombreForm()
    if form.validate_on_submit():
<<<<<<< HEAD
        session['nombre'] = form.nombre.data
=======
        session['nombre'] = form.nombre.data  # Guardar en sesión
>>>>>>> d37ce8f (TR)
        flash('Formulario enviado con éxito!', 'success')
        return redirect(url_for('resultado'))
    return render_template('formulario.html', form=form)

<<<<<<< HEAD
@app.route('/resultado')
def resultado():
    nombre = session.get('nombre', None)
    if nombre is None:
=======
# Ruta para mostrar el resultado
@app.route('/resultado')
def resultado():
    nombre = session.get('nombre', None)  # Obtener de sesión
    if nombre is None:  # Evita errores si no se ha llenado el formulario
>>>>>>> d37ce8f (TR)
        flash('No hay datos en la sesión. Ingresa tu nombre en el formulario.', 'warning')
        return redirect(url_for('formulario'))
    return render_template('resultado.html', nombre=nombre)

@app.route('/about')
def about():
    return render_template('about.html')

<<<<<<< HEAD
# Prueba de conexión con la base de datos
@app.route('/test_db')
def test_db():
    conexion = obtener_conexion()
    return "Conexión exitosa a MySQL" if conexion else "Error en la conexión a MySQL"

# Obtener usuarios en JSON
@app.route('/usuarios', methods=['GET'])
def obtener_usuarios():
    conexion = obtener_conexion()
    if not conexion:
        return jsonify({"error": "No se pudo conectar a la base de datos"}), 500
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    cursor.close()
    conexion.close()
    return jsonify(usuarios)

# Listar usuarios en tabla HTML
@app.route('/usuarios_formulario', methods=['GET'])
def usuarios_tabla():
    conexion = obtener_conexion()
    if not conexion:
        return "Error en la conexión a la base de datos", 500
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    cursor.close()
    conexion.close()
    return render_template('usuarios_formulario.html', usuarios=usuarios)

# Registro de usuario
=======
@app.route('/test_db')
def test_db():
    conexion = obtener_conexion()
    if conexion:
        return "Conexión exitosa a MySQL"
    else:
        return "Error en la conexión a MySQL"

# Ruta para obtener todos los usuarios de la base de datos
@app.route('/usuarios', methods=['GET'])
def obtener_usuarios():
    conexion = obtener_conexion()
    if conexion:
        cursor = conexion.cursor(dictionary=True)  # Para obtener los resultados en formato de diccionario
        cursor.execute("SELECT * FROM usuarios")  # Se corrigió el nombre de la tabla
        usuarios = cursor.fetchall()
        cursor.close()
        conexion.close()
        return jsonify(usuarios)  # Retornar los datos en formato JSON
    else:
        return jsonify({"error": "No se pudo conectar a la base de datos"}), 500

# Ruta para mostrar los usuarios en una tabla HTML
@app.route('/usuarios_formulario', methods=['GET'])
def usuarios_tabla():
    conexion = obtener_conexion()
    if conexion:
        cursor = conexion.cursor(dictionary=True)  # Para obtener los resultados en formato de diccionario
        cursor.execute("SELECT * FROM usuarios")
        usuarios = cursor.fetchall()
        cursor.close()
        conexion.close()
        return render_template('usuarios_formulario.html', usuarios=usuarios)
    else:
        return "Error en la conexión a la base de datos", 500

>>>>>>> d37ce8f (TR)
@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        password = request.form['password']
        password_hash = generate_password_hash(password)

<<<<<<< HEAD
        try:
            conexion = obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute("INSERT INTO usuarios (nombre, email, password) VALUES (%s, %s, %s)",
                           (nombre, email, password_hash))
            conexion.commit()
            cursor.close()
            conexion.close()
            flash('Usuario registrado correctamente', 'success')
            return redirect(url_for('login'))
        except Exception as e:
            flash(f"Error en el registro: {str(e)}", 'danger')

    return render_template('registro.html')

# Inicio de sesión
=======
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO usuarios (nombre, email, password) VALUES (%s, %s, %s)",
                       (nombre, email, password_hash))
        conexion.commit()
        cursor.close()
        conexion.close()
        flash('Usuario registrado correctamente')
        return redirect(url_for('login'))
    return render_template('registro.html')

>>>>>>> d37ce8f (TR)
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
<<<<<<< HEAD
        usuario = Usuario.obtener_por_email(email)

        if usuario and check_password_hash(usuario.password, password):
            login_user(usuario)
            flash('Inicio de sesión exitoso', 'success')
            return redirect(url_for('index'))
        else:
            flash('Email o contraseña incorrectos', 'danger')

    return render_template('login.html')

# Cierre de sesión
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Sesión cerrada correctamente', 'success')
    return redirect(url_for('login'))

# Crear un producto
=======

        usuario = Usuario.obtener_por_email(email)

        if usuario and usuario.verificar_password(password):
            login_user(usuario)
            flash('¡Has iniciado la sesión correctamente!.', 'success')
            return redirect(url_for('index'))  # Redirige a la página de inicio
        else:
            flash('Email o contraseña incorrectos')

    return render_template('login.html')

>>>>>>> d37ce8f (TR)
@app.route('/crear', methods=['GET', 'POST'])
def crear_producto():
    if request.method == 'POST':
        nombre = request.form['nombre']
        precio = request.form['precio']
        stock = request.form['stock']
<<<<<<< HEAD

        if nombre and precio and stock:
            Producto.insertar(nombre, float(precio), int(stock))
            flash('Producto creado exitosamente.', 'success')
            return redirect(url_for('listar_productos'))
        else:
            flash('Todos los campos son obligatorios.', 'danger')

    return render_template('crear_producto.html')

# Listar productos
@app.route('/productos')
def listar_productos():
    productos = Producto.obtener_todos()
    return render_template('productos.html', productos=productos)

# Editar producto
=======
        if nombre and precio and stock:
            Producto.insertar(nombre, float(precio), int(stock))
            flash('Producto creado exitosamente.')
            return redirect(url_for('listar_productos'))
        else:
            flash('Todos los campos son obligatorios.')
    return render_template('crear_producto.html')

@app.route('/productos')
def listar_productos():
    productos = Producto.obtener_todos()  # Asegúrate de que esto devuelva una lista de objetos Producto
    return render_template('productos.html', productos=productos)

>>>>>>> d37ce8f (TR)
@app.route('/editar/<int:id_producto>', methods=['GET', 'POST'])
def editar_producto(id_producto):
    producto = Producto.obtener_por_id(id_producto)
    if request.method == 'POST':
        nombre = request.form['nombre']
        precio = request.form['precio']
        stock = request.form['stock']
        Producto.actualizar(id_producto, nombre, float(precio), int(stock))
<<<<<<< HEAD
        flash('Producto actualizado correctamente.', 'success')
        return redirect(url_for('listar_productos'))
    return render_template('editar_producto.html', producto=producto)

# Eliminar producto
@app.route('/eliminar/<int:id_producto>', methods=['POST'])
def eliminar_producto(id_producto):
    Producto.eliminar(id_producto)
    flash('Producto eliminado correctamente.', 'success')
    return redirect(url_for('listar_productos'))

# Cargar usuario en Flask-Login
=======
        flash('Producto actualizado correctamente.')
        return redirect(url_for('listar_productos'))
    return render_template('editar_producto.html', producto=producto)

@app.route('/eliminar/<int:id_producto>', methods=['GET', 'POST'])
def eliminar_producto(id_producto):
    if request.method == 'POST':
        Producto.eliminar(id_producto)
        flash('Producto eliminado correctamente.')
        return redirect(url_for('listar_productos'))
    producto = Producto.obtener_por_id(id_producto)
    return render_template('eliminar_producto.html', producto=producto)

@app.route('/logout')
@login_required  # Asegúrate de que solo los usuarios autenticados puedan cerrar sesión
def logout():
    logout_user()  # Cierra la sesión del usuario
    flash('Has cerrado sesión exitosamente', 'success')
    return redirect(url_for('index'))  # Redirige al inicio después de cerrar sesión

>>>>>>> d37ce8f (TR)
@login_manager.user_loader
def load_user(user_id):
    return Usuario.obtener_por_id(user_id)

# Ejecutar la aplicación
<<<<<<< HEAD
if __name__ == '__main__':
=======
if __name__ == '__main__':  # Se corrigió '_name_' a '__name__'
>>>>>>> d37ce8f (TR)
    app.run(debug=True)
