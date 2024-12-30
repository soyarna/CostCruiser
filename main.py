from flask import Flask, render_template
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
    return render_template("index.html")

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

if __name__ == '__main__':
    app.run(debug=True)

