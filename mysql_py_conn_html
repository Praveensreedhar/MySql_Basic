from flask import Flask, render_template, url_for
from markupsafe import escape
import mysql.connector
from pprint import pprint
app = Flask(__name__)


mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "T6!v@nd6um",
    database = "my_app"

)

@app.route('/employ')
def employ():
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute("SELECT * FROM Employees")
    employees = mycursor.fetchall()
    return render_template('employ.html', employees=employees)
