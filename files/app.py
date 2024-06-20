from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/country', methods=['POST'])
def country():
    country_name = request.form['country_name']
    api_url = f'https://restcountries.com/v3.1/name/{country_name}'
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()[0]  # Prend le premier pays de la liste
        return render_template('country.html', country=data)
    else:
        return render_template('index.html', error='Country not found')

if __name__ == '__main__':
    app.run(debug=True)
