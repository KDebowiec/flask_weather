# 3e258a0d113b4d8696d163853231010
from flask import request, render_template, Blueprint
import requests

weather_blueprint = Blueprint('weather', __name__)

@weather_blueprint.route('/', methods=['GET', 'POST'])
def get_weather():
    if request.method == 'GET':
        return render_template('weather.html')

    if request.method == 'POST':
        data = ConnectionMixin()

        weather_data = data
        return render_template('weather.html', weather_data=weather_data)

    # http://api.weatherapi.com/v1/current.json?key=<9f76b9f85a4e4c75872150953230710>&q=London


class ConnectionMixin:
    def __init__(self, part_url, city):
        self.part_url = part_url
        self.city = city

    def connecting_to_api(self, method='GET'):
        api_url = self.part_url + self.city
        try:
            if method == 'GET':
                response = requests.get(api_url, headers=None, params=None)
            elif method == 'POST':
                response = requests.post(api_url, headers=None, params=None, data=None)
            elif method == 'PUT':
                response = requests.put(api_url, headers=None, params=None, data=None)
            elif method == 'DELETE':
                response = requests.delete(api_url, headers=None, params=None)
            else:
                return None


            return response


        except requests.exceptions.RequestException as e:
            print(f'Błąd połączenia z API: {str(e)}')
            return None

    def returning_data(self):
        response = self.connecting_to_api()
        if response and response.status_code == 200:
            print(response.json())


connection_instance = ConnectionMixin('http://api.weatherapi.com/v1/current.json?key=3e258a0d113b4d8696d163853231010&q=', 'London')
connection_instance.returning_data()

