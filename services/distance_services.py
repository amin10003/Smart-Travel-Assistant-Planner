import requests


class DistanceService:

    def get_distance(
        self,
        departure,
        destination
    ):

        try:

            url = (
                "https://router.project-osrm.org"
                "/route/v1/driving/"
            )

            query = (
                f"{departure};{destination}"
            )

            response = requests.get(
                url + query
            )

            return {
                "success": False,
                "message":
                "Need coordinates conversion first"
            }

        except Exception as error:

            return {

                "success": False,

                "message":
                str(error)
            }