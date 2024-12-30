# # Koppling till DB och skapa en engine

# import pyodbc
# from sqlalchemy import create_engine, URL

# url = URL.create(drivername="mssql+pyodbc",
#                  host="localhost",
#                  database="costcruiser",
#                  query={"driver": "ODBC Driver 17 for SQL Server"})
# conn = create_engine(url)