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
    <body style="border-top: 60px solid #073858;">
    <div style="text-align: center; margin-top: -60px;">
        <img src="static/image/4update.png" alt="CostCruiser">
    </div>
    <div style="text-align: center;">
        <img src="static/image/1update.png" alt="CostCruiser">
    </div>
        <nav style = "text-align:center;">
        <label for="category"></label>
        <select style= "padding:10px 30px"; name="forma" onchange="window.location.href=this.value;">
            <option value="" selected disabled hidden>Select a category</option>
            <option value="/electronics">Electronics</option>
            <option value="/outdoor_and_gardening">Outdoor & Gardening</option>
            <option value="/dog_supplies">Dog supplies</option>
            <option value="/fitness_accessories">Fitness Accessories</option>
            <option value="/home-and-kitchen">Home & Kitchen</option>
        </select>
        <h4 style = "text-align:center;">Bon Voyage</h4>
        </nav>
        {body}
    </body>
    </html>
    """
