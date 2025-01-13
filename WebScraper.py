import requests
from bs4 import BeautifulSoup

def getproduct(URL, searchinput, categoryinput):
    url_input = 'https://www.prisjakt.nu/search?search=iphone' + searchinput
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url_input, headers=headers)

with open("prisjakt_iphone.html", "r") as prisjakt:
    code = BeautifulSoup(prisjakt, "html.parser")

productdiv_list = code.find_all('li', {'data-test': 'ProductGridCard'})

for product in productdiv_list:
    product_name = product.find('span', {'data-testid': 'ProductName'})
    category_name = product.find('span', {'data-testid': 'Category'})
    price = product.find('span', {'class': 'Text--q06h0j igDZdP'})
    image_url = product.find('img', {'data-testid': 'ProductCardImage'})

    print(product_name)
    print(category_name)
    print(price)
    print(image_url)

