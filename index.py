def index(title, body):
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <link rel="shortcut icon" type="image/x-icon" href="/static/image/2.ico" />
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{title}</title>
        <link rel="stylesheet" type="text/css" href="/static/styles.css">
    </head>
    <body class="border">
    <div class="header">
        <img src="static/image/4update.png" alt="CostCruiser">
    </div>
    <div class="hero">
        <img src="static/image/1update.png" alt="CostCruiser">
    </div>
    <h4 class="bon">Bon Voyage</h4>
        <nav class="nav">
        <label for="category"></label>
        <select class="dropdown" onchange="window.location.href=this.value;">
            <option value="" selected disabled hidden>&#x2693</option>
            <option class="values" value="/electronics">Electronics</option>
            <option class="values" value="/outdoor_and_gardening">Outdoor & Gardening</option>
            <option class="values" value="/dog_supplies">Dog supplies</option>
            <option class="values" value="/fitness_accessories">Fitness Accessories</option>
            <option class="values" value="/home-and-kitchen">Home & Kitchen</option>
        </select>
        </nav>
        {body}
    </body>
    </html>
    """
