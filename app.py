from flask import Flask, render_template, jsonify, request
from flask_cors import CORS, cross_origin
import requests
from bs4 import BeautifulSoup
import re
#import pandas as pd

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/117.0"
}

app = Flask(__name__)

#default landing page
@app.route("/")
def home():
    return render_template("home.html")

@app.route('/standings_data', methods=['GET'])
def get_data():
    option = request.args.get('option')
    url = 'https://www.atlanticuniversitysport.com/sports/'  
  
    if option == 'f':
        url = url + 'wice/2023-24/standings'
    else:
        url = url + 'mice/2023-24/standings'

    # Make the request
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Raise an error for bad responses

    # Parse the HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the correct table (this assumes you want the first table, adjust if needed)
    table = soup.find('table')

    # Check if the table was found
    if not table:
        raise ValueError("Table not found")

    # Find all rows in the table
    rows = table.find_all('tr')

    # Extract data
    data = []
    for row in rows:
        cols = row.find_all('td')
        if len(cols) > 0:
            # Extract text for each column
            row_data = [col.get_text(strip=True) for col in cols]
            data.append(row_data)

    # Update the data with extracted team names
    updated_data = []
    for row in data:
        if len(row) > 0:
            team_name = extract_team_name(row)
            updated_row = [team_name] + row[1:]  # Replace the first column with the extracted team name
            updated_data.append(updated_row)
        else:
            updated_data.append(row)  # Keep the header row unchanged
    
    

    return jsonify(updated_data)

#helper function to remove excess data from data
def extract_team_name(entry):
    match = re.match(r'([^\d]+)', entry[0])
    if match:
        return match.group(1).strip()
    
    return "Team name not found"

#main landing page for the schedule
@app.route("/wschedule")
def wschedule():
    return render_template("wschedule.html")

@app.route("/schedule_data")
def get_schedule():
    url = 'https://www.atlanticuniversitysport.com/sports/wice/2024-25/schedule?confonly=1'
    
    response = requests.get(url, headers=headers)

    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')
    
    table = soup.find('table')
    rows = table.find_all('tr')
    header_data = rows[0]
    data = []


    return ""

#main landing page for the standings
@app.route("/wstandings")
def wstandings():
    return render_template("wstandings.html")

@app.route("/mstandings")
def mstandings():
    return render_template("mstandings.html")

#this *may* need to be removed when moving to 
#production, depending on the production server
if __name__ == '__main__':
    app.run(debug=True)