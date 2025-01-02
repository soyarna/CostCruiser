def index(title, body):
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <link rel="shortcut icon" type="image/x-icon" href="/static/image/2.ico" />
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{title}</title>
        <link rel="stylesheet" type="text/css" href="styles.css">
    </head>
    <body style="border-top: 60px solid #073858;">
    <div style="text-align: center; margin-top: -60px;">
        <img src="static/image/4update.png" alt="CostCruiser">
    </div>
    <div style="text-align: center;">
        <img src="static/image/1update.png" alt="CostCruiser">
    </div>
    <h4 style = "text-align:center;">Bon Voyage</h4>
        <nav style="margin-top: -462px; padding-left: 10px;">
        <label for="category"></label>
        <select  style= "appearance: none; border: none; background-color: transparent; font-size: 36px; width: 50px;" name="forma" onchange="window.location.href=this.value;">
            <option value="" selected disabled hidden>&#x2693</option>
            <option style= "font-size: 15px;" value="/electronics">Electronics</option>
            <option style= "font-size: 15px;" value="/outdoor_and_gardening">Outdoor & Gardening</option>
            <option style= "font-size: 15px;" value="/dog_supplies">Dog supplies</option>
            <option style= "font-size: 15px;" value="/fitness_accessories">Fitness Accessories</option>
            <option style= "font-size: 15px;" value="/home-and-kitchen">Home & Kitchen</option>
        </select>
        </nav>
        {body}
    </body>
    </html>
    """
