from flask import Flask, render_template, jsonify, render_template_string
from sqlalchemy.orm import sessionmaker
import pyodbc
from sqlalchemy import create_engine, URL, text
from index import index

url = URL.create(drivername="mssql+pyodbc",
                 host="localhost",
                 database="costcruiser",
                 query={"driver": "ODBC Driver 17 for SQL Server"})
conn = create_engine(url)

Session = sessionmaker(bind=conn)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string(index("Costcruiser", ""))

@app.route('/electronics')
def category1():
    with Session() as session:
        result = session.execute(text("""
            SELECT 
	            s.store_name,
	            p.product_name,
	            CAST(p.price AS INT) AS price,
	            CASE
		            WHEN p.ratings IS NULL THEN 'N/A'
		            ELSE CAST(p.ratings AS VARCHAR)
	            END AS ratings,
	            p.image,
                p.no_ratings,
	            p.website_url
            FROM Product AS p
        INNER JOIN Category AS c ON p.category_id = c.category_id
        INNER JOIN Store AS s ON p.store_id = s.store_id
        WHERE c.category_id = 1
        ORDER BY p.no_ratings DESC;
        """)).fetchall()

        # Skapa HTML-struktur för att visa produkter
        html_content = """
        <h1>Electronics</h1>
        <table border="1">
            <tr>
                <th>Store Name</th>
                <th>Product Name</th>
                <th>Price</th>
                <th>Ratings</th>
                <th>Image</th>
            </tr>
        """
        
        # Lägg till produkter i HTML-tabellen
        for row in result:
            html_content += f"""
            <tr>
                <td>{row.store_name}</td>
                <td><a href="{row.website_url}" target="_blank">{row.product_name}</a></td>
                <td>{row.price}:-</td>
                <td>{row.ratings}</td>
                <td><img src="{row.image}" alt="Image coming soon"></td>
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
    with Session() as session:
        #get product info
        result = session.execute(text("""
            SELECT 
	            s.store_name,
	            p.product_name,
	            CAST(p.price AS INT) AS price,
	            CASE
		            WHEN p.ratings IS NULL THEN 'N/A'
		            ELSE CAST(p.ratings AS VARCHAR)
	            END AS ratings,
	            p.image,
                p.no_ratings,
	            p.website_url
            FROM Product AS p
        INNER JOIN Category AS c ON p.category_id = c.category_id
        INNER JOIN Store AS s ON p.store_id = s.store_id
        WHERE c.category_id = 5
        ORDER BY p.no_ratings DESC;
        """)).fetchall()

       # Skapa HTML-struktur för att visa produkter
        html_content = """
        <h1>Dog supplies</h1>
        <table border="1">
            <tr>
                <th>Store Name</th>
                <th>Product Name</th>
                <th>Price</th>
                <th>Ratings</th>
                <th>Image</th>
            </tr>
        """
        
        # Lägg till produkter i HTML-tabellen
        for row in result:
            html_content += f"""
            <tr>
                <td>{row.store_name}</td>
                <td><a href="{row.website_url}" target="_blank">{row.product_name}</a></td>
                <td>{row.price}:-</td>
                <td>{row.ratings}</td>
                <td><img src="{row.image}" alt="Image coming soon"></td>
            </tr>
            """
        
        html_content += "</table>"


    return render_template_string(index("Dog Supplies", html_content))

@app.route('/fitness_accessories')
def category4():
    return """
    <h1>SPORTS</h1>
    """

@app.route('/home-and-kitchen')
def category5():
    with Session() as session:
        result = session.execute(text("""
            SELECT 
	            s.store_name,
	            p.product_name,
	            CAST(p.price AS INT) AS price,
	            CASE
		            WHEN p.ratings IS NULL THEN 'N/A'
		            ELSE CAST(p.ratings AS VARCHAR)
	            END AS ratings,
	            p.image,
                p.no_ratings,
	            p.website_url
            FROM Product AS p
        INNER JOIN Category AS c ON p.category_id = c.category_id
        INNER JOIN Store AS s ON p.store_id = s.store_id
        WHERE c.category_id = 4
        ORDER BY p.no_ratings DESC;
        """)).fetchall()

        # Skapa HTML-struktur för att visa produkter
        html_content = """
        <h1>Home and Kitchen</h1>
        <table border="1">
            <tr>
                <th>Store Name</th>
                <th>Product Name</th>
                <th>Price</th>
                <th>Ratings</th>
                <th>Image</th>
            </tr>
        """
        
        # Lägg till produkter i HTML-tabellen
        for row in result:
            html_content += f"""
            <tr>
                <td>{row.store_name}</td>
                <td><a href="{row.website_url}" target="_blank">{row.product_name}</a></td>
                <td>{row.price}:-</td>
                <td>{row.ratings}</td>
                <td><img src="{row.image}" alt="Image coming soon"></td>
            </tr>
            """
        
        html_content += "</table>"

    # Returnera HTML-innehållet
    return html_content