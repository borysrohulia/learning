import pprint
import requests
from dateutil.parser import parse

class YahooWeatherForecast:

    def __init__(self):
        self._city_cache = {}

    def get(self, city):
        if city in self._city_cache:
            return self._city_cache[city]
        url = 'https://api.weatherbit.io/v2.0/current?city=Raleigh,NC&key=API_KEY'
        print("sending request")
        data = requests.get(url).json()
        forecast_data = data["query"]["results"]["channel"]["item"]["forecast"]
        forecast = []
        for day_data in forecast_data:
            forecast.append({
                "date": parse(day_data["date"]),
                "high_temp": day_data["high"]
            })
        self._city_cache[city] = forecast
        return forecast

class CityInfo:
    def __init__(self, city, weather_forecast=None):
        self.city = city
        self.weather_forecast = weather_forecast or YahooWeatherForecast

    def weather_forecast(self):
        return self.weather_forecast.get(self.city)

def _main():
    weather_forecast = YahooWeatherForecast()
    for i in range(5):
        city_info = CityInfo("Moscow", weather_forecast=weather_forecast)
        forecast = city_info.weather_forecast()
    pprint.pprint(forecast)

if __name__ == "__main__":
    _main()