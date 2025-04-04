from flask import Flask, render_template, request, Response, jsonify, redirect, url_for
import database as dbase 
from product import Producto  

app= Flask(__name__)
db= dbase.dbConection() 

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/products', methods=['POST'])
def addproduct():
    products = db['products'] #
    nombre = request.form['nombre'] 
    titulo= request.form['titulo'] 
    autor=request.form['autor'] 

    if nombre and titulo and autor:
        products = products(nombre,titulo,autor)
        products.insert_one(products.paraConexiondb())
        Response= jsonify({
            'nombre': nombre,
            'autor':autor,
            'titulo':titulo
        })
        return redirect(url_for('home'))
    else:
        return notfound()
    
@app.errorhandler(404)
def notfound (error=None):
    message={
        'mensaje': 'no encontreado' + request.url,
        'status': '404 not found'
    }
    Response =jsonify(message)
    Response.status_code=404
    return Response
if __name__ == '__main__':
    app.run(debug=True, port=5000)