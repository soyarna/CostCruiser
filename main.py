from flask import Flask
import pyodbc
from sqlalchemy import create_engine, URL

url = URL.create(drivername="mssql+pyodbc",
                 host="localhost",
                 database="costcruiser",
                 query={"driver": "ODBC Driver 17 for SQL Server"})
conn = create_engine(url)

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>Hej, världen!</h1>
    <h3>Categories:</h3>
    <a href="/electronics">Electronics</a>
    <a href="/outdoor_and_gardening">Outdoor</a>
    <a href="/dog_supplies">Dog toys</a>
    <a href="/fitness_accessories">Sport</a>
    <a href="/home-and-kitchen">Home and Kitchen</a>
    """

@app.route('/electronics')
def category1():
    return """
    <h1>ELEKTRONIK</h1>
    """

@app.route('/outdoor_and_gardening')
def category2():
    return """
    <h1>OUTDOOR</h1>
    """

@app.route('/dog_supplies')
def category3():
    return """
    <h1>woofwoof</h1>
    """

@app.route('/fitness_accessories')
def category4():
    return """
    <h1>SPORTS</h1>
    """

@app.route('/home-and-kitchen')
def category5():
    return """
    <h1>Knives to kill you spouse</h1>
    """



