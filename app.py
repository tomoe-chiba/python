from flask import Flask,redirect,url_for,render_template, request, flash
import jinja2

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    titulo='Hola Mundo!'
    return render_template('login.html', ejemplo=titulo)

@app.route('/procesar_credenciales',methods=['POST'])
def procesarCredenciales():
    if request.method== 'POST':
        datos = request.form
        correo = datos['txtCorreo']
        password = datos['txtPassword']
        return "Mi correo es: " + password

        # if(correo=="" or password==""):
        #     flash("Debe completar los campos", "alerta")
        # else:
        #     flash("Se han recibido las credenciales", "correcto")


if __name__ == '__main__':
    app.run(port=5000,debug=True) 