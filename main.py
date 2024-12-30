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
    <a href="/outdoor">Outdoor</a>
    <a href="/dog-toys">Dog toys</a>
    <a href="/sports">Sport</a>
    <a href="/Home-and-kitchen">Home and Kitchen</a>
    <a href="/Gardening">Gardening</a>
    """

@app.route('/electronics')
def category1():
    return """
    <h1>ELEKTRONIK</h1>
    """

@app.route('/outdoor')
def category2():
    return """
    <h1>OUTDOOR</h1>
    """

@app.route('/dog-toys')
def category3():
    return """
    <h1>woofwoof</h1>
    """

@app.route('/sports')
def category4():
    return """
    <h1>SPORTS</h1>
    """

@app.route('/Home-and-kitchen')
def category5():
    return """
    <h1>Knives to kill you spouse</h1>
    """


@app.route('/Gardening')
def category6():
    return """
    <h1>Gardening</h1>
    """

# hej hej
#hej hej