def index(title, body):
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <link rel="shortcut icon" type="image/x-icon" href="/static/image/2.ico" />
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{title}</title>
    </head>
    <body>
        <h1>Welcome to CostCruiser</h1>
        <h3>Categories:</h3>
        <nav>
            <a href="/electronics">Electronics</a>
            <a href="/outdoor_and_gardening">Outdoor & Gardening</a>
            <a href="/dog_supplies">Dog supplies</a>
            <a href="/fitness_accessories">Fitness Accessories</a>
            <a href="/home-and-kitchen">Home & Kitchen</a>
        </nav>
        {body}
    </body>
    </html>
    """
