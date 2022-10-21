from cProfile import run
from distutils.log import debug
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('sitio/index.html')

@app.route('/libros')
def libros():
    return render_template('sitio/libros.html')

@app.route('/nosotros')
def nosotros():
    return render_template('sitio/nosotros.html')

@app.route('/txt')
def txt():
    return render_template('sitio/txt.html')

if __name__ == '__main__':
      app.run(debug=True)
