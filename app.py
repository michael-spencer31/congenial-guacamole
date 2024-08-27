from flask import Flask, render_template
from flask_cors import CORS, cross_origin
import requests
from bs4 import BeautifulSoup
# import pandas as pd

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/117.0"
}

app = Flask(__name__)

@app.route("/")
def home():

    url = 'https://www.atlanticuniversitysport.com/sports/wice/2023-24/standings'
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table')
    print(table)
    return render_template("home.html", value=table)

if __name__ == '__main__':
    app.run(debug=True)