from flask import Flask, render_template
from sqlalchemy.orm import sessionmaker
import pyodbc
from sqlalchemy import create_engine, URL, text

url = URL.create(drivername="mssql+pyodbc",
                 host="localhost",
                 database="costcruiser",
                 query={"driver": "ODBC Driver 17 for SQL Server"})
conn = create_engine(url)

Session = sessionmaker(bind=conn)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/electronics')
def category1():
    with Session() as session:
        result = session.execute(text("""
            SELECT p.product_name, CAST(p.price AS INT) AS price
            FROM Product AS p
            INNER JOIN Category AS c ON p.category_id = c.category_id
            WHERE c.category_id = 1
        """)).fetchall()

        # Skapa HTML-struktur för att visa produkter
        html_content = """
        <h1>Electronics</h1>
        <table border="1">
            <tr>
                <th>Product Name</th>
                <th>Price</th>
            </tr>
        """
        
        # Lägg till produkter i HTML-tabellen
        for row in result:
            html_content += f"""
            <tr>
                <td>{row.product_name}</td>
                <td>{row.price}:-</td>
            </tr>
            """
        
        html_content += "</table>"

    # Returnera HTML-innehållet
    return html_content


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

