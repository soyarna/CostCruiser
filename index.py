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
        <label for="category">Start Cruising:</label>
        <select name="forma" onchange="window.location.href=this.value;">
            <option value="" selected disabled hidden>Select a category</option>
            <option value="/electronics">Electronics</option>
            <option value="/outdoor_and_gardening">Outdoor & Gardening</option>
            <option value="/dog_supplies">Dog supplies</option>
            <option value="/fitness_accessories">Fitness Accessories</option>
            <option value="/home-and-kitchen">Home & Kitchen</option>
        </select>
        </nav>
        {body}
    </body>
    </html>
    """
