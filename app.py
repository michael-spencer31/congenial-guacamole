from flask import Flask, render_template
from flask_cors import CORS, cross_origin
import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/117.0"
}

app = Flask(__name__)

#default landing page
@app.route("/")
def home():

    url = 'https://www.atlanticuniversitysport.com/sports/wice/2023-24/standings'

    #pass in headers with the request so we don't get blocked
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table')
    print(table)
    return render_template("home.html", value=table)

#main landing page for the schedule
@app.route("/schedule")
def schedule():
    return render_template("schedule.html")

#main landing page for the standings
@app.route("/standings")
def standings():
    return render_template("standings.html")

#this *may* need to be removed when moving to 
#production, depending on the production server
if __name__ == '__main__':
    app.run(debug=True)