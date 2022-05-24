import requests


class WeatherInfo:
    def __init__(self, city_name: str, api_key: str, units: str = 'metric'):
        self.city_name = city_name
        self.api_key = api_key
        self.units = units
        self.response = None
        self.weather_symbol = {
            '01': '☀',
            '02': '🌤',
            '03': '⛅',
            '04': '☁',
            '09': '🌦',
            '10': '🌧',
            '11': '⛈',
            '13': '🌨❄',
            '50': '🌫'
        }
        self.base_url = "http://api.openweathermap.org/data/2.5/weather?"

    def save_api_response(self):
        complete_url = f"{self.base_url}appid={self.api_key}&q={self.city_name}&units={self.units}"
        self.response = requests.get(complete_url).json()

    def get_weather_info(self):
        if self.response is None:
            self.save_api_response()
        print(self.response)

        if self.response['cod'] != '404':
            return self.weather_symbol[self.response['weather'][0]['icon'][0:2]], self.response['main']['temp']
        else:
            raise ConnectionError(f"Erroneous details provided, please check :\n"
                                  f"City Name : {self.city_name}\n"
                                  f"API key   : {self.api_key}\n"
                                  f"Units     : {self.units}")
