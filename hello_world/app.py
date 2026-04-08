from flask import Flask

app = Flask(__name__)

@app.route('/') # home or root of site

def index():
    return '<html><head><title>HELLO WORLD</title></head><body><h1>Hello, World!</h1><p>Ir a <a href="/about">About</a></p></body></html>'

@app .route('/about') # about page

def about():
    return '<html><head><title>About this page</title></head><body><h1>Everything about this website. Back to <a href="/">Hello world</a></h1></body></html>'

if __name__ == '__main__':
    app.run(debug=True) # run the app in debug mode