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
    return render_template_string(index("CostCruiser", ""))

def render_category(category_id, category_name):
    with Session() as session:
        # Query the database
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
            WHERE c.category_id = :category_id
            ORDER BY p.no_ratings DESC;
        """), {"category_id": category_id}).fetchall()

        # Generate rows for the table
        rows = "".join(f"""
        <tr>
                <td class="bordercat">{row.store_name}</td>
                <td class="bordercat"><a class="bordercatname" href="{row.website_url}" target="_blank">{row.product_name}</a></td>
                <td class="bordercat">{row.price}:-</td>
                <td class="bordercat">{row.ratings}</td>
                <td class="bordercatimg"><img src="{row.image}" alt="Image coming soon" onerror="this.onerror=null; this.src='static/image/missing_image.png';"></td>
        </tr>
        """ for row in result)

    # Read the template
    with open("category_template.html", "r") as file:
        template = file.read()

    # Replace placeholders and return the final HTML
    return template.replace("{{category}}", category_name).replace("{{rows}}", rows)

@app.route('/electronics')
def electronics():
    return render_category(category_id=1, category_name="Electronics")


@app.route('/garden_and_outdoors')
def garden_and_outdoors():
    return render_category(category_id=3, category_name="Garden & Outdoor")

@app.route('/dog_supplies')
def dog_supplies():
    return render_category(category_id=5, category_name="Dogs Supplies")

@app.route('/fitness_accessories')
def fitness_accessories():
    return render_category(category_id=2, category_name="Fitness Accessories")

@app.route('/home_and_kitchen')
def home_and_kitchen():
    return render_category(category_id=4, category_name="Home & Kitchen")