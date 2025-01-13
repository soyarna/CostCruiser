from sqlalchemy import text

def searchquerybody(session, search, WHERE, ORDERBY, LIMIT):
    # Construct the SQL query dynamically
    query = text(f"""
        SELECT TOP {LIMIT}
            product_id,
            product_name,
            image,
            website_url,
            CAST(price AS INT) AS price,
            CAST(discount_price AS INT) AS discount_price,
            ratings,
            no_ratings,
            product_description,
            category_name,
            store_name
        FROM product p
        JOIN Category c ON c.category_id = p.category_id
        JOIN Store s ON s.store_id = p.store_id
        WHERE price > 0 AND discount_price > 0 AND LOWER(product_name) LIKE LOWER('%{search}%'){WHERE}
        ORDER BY {ORDERBY}
    """)
    
    # Execute the query
    results = session.execute(query).fetchall()
    return results