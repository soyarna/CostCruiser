import re
import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, request, redirect, url_for, jsonify, session, flash

def getproduct(searchinput):
    url_input = 'https://www.prisjakt.nu/search?search=' + searchinput
    # headers = {'User-Agent': 'Mozilla/5.0'}
    # response = requests.get(url_input, headers=headers)

    # code = BeautifulSoup(response.text, "html.parser")
    print("url: ", url_input)
    with open("prisjakt_iphone.html", "r") as prisjakt:
        code = BeautifulSoup(prisjakt, "html.parser")

    productdiv_list = code.find_all('li', {'data-test': 'ProductGridCard'})

    products = []

    for product in productdiv_list:
        product_name = product.find('span', {'data-testid': 'ProductName'})
        category_name = product.find('span', {'data-testid': 'Category'})
        price = product.find('span', {'class': 'Text--q06h0j igDZdP'})
        rating = product.find('div', {'data-testid': 'Rating'})
        no_rating = product.find('span', {'class': 'Counter-sc-0-1 cNVjGL'})
        image_url = product.find('img', {'data-testid': 'ProductCardImage'})

        product_name = product_name.text
        category_name = category_name.text
        price = re.sub(r"[^\d]", "", price.text.strip())
        image_url = image_url['src']
        rating = rating['aria-label'] if rating and 'aria-label' in rating.attrs else ""
        no_rating = no_rating.text.strip() if no_rating else ""
        rating = rating[:3]

        products.append({
            "product_name": product_name,
            "category_name": category_name,
            "price": price,
            "image_url": image_url,
            "rating": rating,
            "number_of_ratings": no_rating
        })

    return products




