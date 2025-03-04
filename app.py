from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, MLOps!"

@app.route('/abd')
def abd():
    return "hello im abdullah bin faisal"

if __name__ == '__main__':
    app.run(debug=True)
