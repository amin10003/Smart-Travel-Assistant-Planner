import requests
import os
from dotenv import load_dotenv


load_dotenv()


class WeatherService:

    def __init__(self):

        self.api_key = os.getenv("API_KEY")

        self.base_url = (
            "https://api.openweathermap.org/data/2.5/weather"
        )

    def get_weather(self, city):

        try:

            response = requests.get(
                self.base_url,
                params={
                    "q": city,
                    "appid": self.api_key,
                    "units": "metric"
                }
            )

            data = response.json()

            if response.status_code != 200:

                return {
                    "success": False,
                    "message": data.get(
                        "message",
                        "Unable to fetch weather"
                    )
                }

            return {
                "success": True,
                "city": data["name"],
                "temperature": data["main"]["temp"],
                "condition": data["weather"][0]["main"],
                "humidity": data["main"]["humidity"]
            }

        except Exception as error:

            return {
                "success": False,
                "message": str(error)
            }