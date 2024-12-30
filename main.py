# from flask import Flask

# # Koppling till DB och skapa en engine

# import pyodbc
# from sqlalchemy import create_engine, URL

# url = URL.create(drivername="mssql+pyodbc",
#                  host="localhost",
#                  database="costcruiser",
#                  query={"driver": "ODBC Driver 17 for SQL Server"})
# conn = create_engine(url)

# Skapa en applikation: Flask(name) initierar applikationen.

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return """<h1>Hej, världen!</h1>
#  <h3>Hej, världen!</h3>   """