import requests


class GeocodeService:

    def __init__(self):

        self.url = (
            "https://nominatim.openstreetmap.org/search"
        )

    def get_coordinates(
        self,
        place
    ):

        try:

            response = requests.get(

                self.url,

                params={
                    "q": place,
                    "format": "json",
                    "limit": 1
                },

                headers={
                    "User-Agent":
                    "SmartTravelAssistant"
                }
            )

            data = response.json()

            if not data:

                return {

                    "success": False,

                    "message":
                    "Place not found"
                }

            return {

                "success": True,

                "latitude":
                float(
                    data[0]["lat"]
                ),

                "longitude":
                float(
                    data[0]["lon"]
                )
            }

        except Exception as error:

            return {

                "success": False,

                "message":
                str(error)
            }