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
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    </head>
    <body class="border">
    <div class="lower_border"></div>
    <div class="header">
        <img src="static/image/4update.png" alt="CostCruiser">
    </div>
    <div class="hero">
        <img src="static/image/1update.png" alt="CostCruiser">
    </div>
    <h4 class="bon">Pick a category, set sail, and bon voyage with CostCruiser</h4>
    <h4 class="bon2">We will navigate and find the best prices across the seven seas!<br>Drop the anchor for categories</br></h4>
        <nav class="nav">
        <label for="category"></label>
        <select class="dropdown" onchange="window.location.href=this.value;">
            <option value="" selected disabled hidden>&#x2693;</option>
            <option class="values" value="/electronics">Electronics</option>
            <option class="values" value="/outdoor_and_gardening">Outdoor & Gardening</option>
            <option class="values" value="/dog_supplies">Dog supplies</option>
            <option class="values" value="/fitness_accessories">Fitness Accessories</option>
            <option class="values" value="/home-and-kitchen">Home & Kitchen</option>
        </select>
        </nav>
        <div class="social-media-icons">
        <a href="https://www.linkedin.com/" target="_blank" class="social-icon">
            <i class="fa fa-linkedin"></i>
        </a>
        <a href="https://twitter.com/" target="_blank" class="social-icon">
            <i class="fa fa-twitter"></i>
        </a>
        <a href="https://www.facebook.com/" target="_blank" class="social-icon">
            <i class="fa fa-facebook"></i>
        </a>
        </div>
        <div class="klarna-icon">
            <a href="https://www.klarna.com/se/villkor/" target="_blank">
                <img src="static/image/Klarna.png" alt="Klarna">
            </a>
        </div>
        {body}
    </body>
    </html>
    """
