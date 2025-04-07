from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return 'The Parliament Jos'
    
@app.route('/Ministers')
def about():
    return 'About the Parliament Jos.'
    
@app.route('/Programmes')
def about():
    return 'About the Parliament Jos.'
    
@app.route('/Message Repository')
def about():
    return 'About the Parliament Jos.'
    
@app.route('/about')
def about():
    return 'About the Parliament Jos.'


if __name__ == '__main__':
    app.run(debug=True)

