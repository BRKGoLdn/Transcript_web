from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/setting')
def setting():
    return render_template('setting.html')

@app.route('/transcript')
def transcript():
    return render_template('transcript.html')

@app.route('/login',methods = ['POST', 'GET'])
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)