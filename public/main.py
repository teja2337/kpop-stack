from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


database = {'suresh': 'suresh@12', 'gopal': 'gopal@12', 'teja': 'teja@12'}


@app.route('/login', methods=['GET', 'POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if username not in database:
        return render_template('index.html', Login='Invalid username or password !')
    else:
        if database[username] != password:
            return render_template('index.html', Login='Invalid username or password !')
        else:
            return render_template('home.html', user=username)


if __name__ == '__main__':
    app.run()
