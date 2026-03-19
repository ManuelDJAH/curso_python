from flask import Flask

app = Flask(__name__)

@app.route('/') # home or root of site

def index():
    return 'Hello, World!' # response to request

@app .route('/about') # about page

def about():
    return 'This is the about page.' # response to request

if __name__ == '__main__':
    app.run(debug=True) # run the app in debug mode