from flask import Flask, render_template, url_for
from markupsafe import escape
import mysql.connector
from pprint import pprint
app = Flask(__name__)


mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "passwor@123",
    database = "my_app"

)

mycursor = mydb.cursor(dictionary=True)
mycursor.execute("SELECT * FROM Employees")
employees = mycursor.fetchall()
pprint(employees)
