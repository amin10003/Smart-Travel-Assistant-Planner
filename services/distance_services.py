import requests
from services.geocode_service import GeocodeService


class DistanceService:

    def __init__(self):

        self.geo = GeocodeService()

    def get_distance(
        self,
        departure,
        destination
    ):

        try:

            start = self.geo.get_coordinates(
                departure
            )

            end = self.geo.get_coordinates(
                destination
            )

            if not start["success"]:

                return start

            if not end["success"]:

                return end

            start_lon = start["longitude"]
            start_lat = start["latitude"]

            end_lon = end["longitude"]
            end_lat = end["latitude"]

            url = (

                "https://router.project-osrm.org"

                f"/route/v1/driving/"

                f"{start_lon},{start_lat};"

                f"{end_lon},{end_lat}"

            )

            response = requests.get(
                url
            )

            data = response.json()

            if (
                data.get("code")
                !=
                "Ok"
            ):

                return {

                    "success": False,

                    "message":
                    "Unable to calculate route"
                }

            meters = (

                data["routes"][0]

                ["distance"]

            )

            km = round(
                meters / 1000,
                2
            )

            return {

                "success": True,

                "distance": km
            }

        except Exception as error:

            return {

                "success": False,

                "message":
                str(error)
            }