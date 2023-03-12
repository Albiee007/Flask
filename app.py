from flask import Flask, render_template, request, redirect, session
from flask_mysqldb import MySQL
import MySQLdb.cursors

app = Flask(__name__)
app.secret_key = '45915d69b58f3d8951bc6bba00e54dca6ae4bce50f5e65af'

# MySQL configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'AlbiEe'
app.config['MYSQL_PASSWORD'] = '3ples007'
app.config['MYSQL_DB'] = 'share_market'

mysql = MySQL(app)
@app.route('/home')
    

@app.route('/')
def home():
    if 'username' in session:
        return render_template('home.html', username=session['username'])
    else:
        return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST'and 'username' in request.form and 'password' in request.form:
        # Get form data
        username = request.form['username']
        password = request.form['password']

        # Connect to MySQL and execute query
        cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
        user = cur.fetchone()

        # Check if user exists in MySQL
        if user:
            session['username'] = user['username']
            cur.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
            mysql.connection.commit()
            cur.close()
            #return redirect('/home')
            return render_template('home.html')
        else:
            return render_template('login.html', error='Invalid username or password')

    #return render_template('login.html')

#To debug
if __name__ == '__main__':
    app.run(debug=True)
#change for git 


