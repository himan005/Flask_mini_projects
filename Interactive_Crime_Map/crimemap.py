from flask import Flask, render_template, request
from DBOperations import DBHelper

app = Flask(__name__)

db = DBHelper()

@app.route('/')
def home():
    try:
        data = db.get_all_inputs()
    except Exception as e:
        print(e)
        data = None
    return render_template('home.html', data = data)


@app.route('/add', methods = ['POST'])
def add():
    try:
        data = request.form.get('userinput')
        db.add_input(data)
    except Exception as e:
        print(e)
    return home()

@app.route('/clear')
def clear():
    try:
        db.clean_all()
    except Exception as e:
        print(e)
    return home()

if __name__ == '__main__':
    app.run(debug= True)


