from flask import Flask, render_template, request, redirect, url_for, jsonify
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

def render_category(category_id, category_name):    
    with Session() as session:
        result = session.execute(text("""
            EXEC GetCategoryProducts :category_id
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
    with open("templates/category_template.html", "r") as file:
        template = file.read()

    # Replace placeholders and return the final HTML
    return template.replace("{{category}}", category_name).replace("{{rows}}", rows)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/search')
def search():

    search = request.args.get('searchinput')

    with Session() as session:
        result = session.execute(text("""
            SELECT top 100
                product_id,
                image,
                product_name,
                FORMAT(price, '0') AS price,
                website_url
            FROM product
            WHERE LOWER(product_name) LIKE LOWER(:search)
        """), {"search": f"%{search}%"}).fetchall()

        # Generate HTML rows for products
        rows = "".join(f"""
        <div class="product-box" onclick="window.location.href='/product/{row.product_id}';">
            <img src="{row.image}" alt="Image coming soon" onerror="this.onerror=null; this.src='static/image/missing_image.png';">
            <h3>{row.product_name}</h3>
            <p>{row.price} SEK</p>
            <button class="buybutton" onclick="window.location.href='{row.website_url}';">!BUY NOW!</button>
        </div>
        """ for row in result)

    return render_template("search.html", rows=rows)

@app.route('/product/<product_id>')
def productoverview(product_id):
    with Session() as session:
        result = session.execute(text("""
            SELECT  
                product_id,
                product_name,
                image,
                website_url,
                FORMAT(price, '0') AS price,
                FORMAT(discount_price, '0') AS discount_price,
                ratings,
                no_ratings,
                product_description,
                store_name,
                category_name
            FROM Product p
            JOIN Category c ON c.category_id = p.category_id
            JOIN Store s ON s.store_id = p.store_id
            WHERE product_id = :product_id
        """), {"product_id": product_id}).fetchone()

        product = {
            "id": result.product_id,
            "name": result.product_name,
            "image": result.image,
            "website_url": result.website_url,
            "price": result.price,
            "discount_price": result.discount_price,
            "ratings": result.ratings,
            "no_ratings": result.no_ratings,
            "description": result.product_description,
            "store_name": result.store_name,
            "category_name": result.category_name
        }

    return render_template("product.html", product=product)



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

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        try:
            with Session() as session:
                session.execute(text("""
                    INSERT INTO [User] (email, password)
                    VALUES (:email, :password)
                """), {"email": email, "password": password})
                session.commit()
            return redirect(url_for('login'))
        
        except Exception as e:
            return f"Error: {e}"
        
    return render_template("register.html")