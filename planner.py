from models.trip import Trip
from services.weather_api import WeatherService
from services.fare_services import FareService
from services.distance_services import DistanceService
from database.database import DatabaseManager


class TravelPlanner:

    def __init__(self):

        self.weather = WeatherService()

        self.fare = FareService()

        self.distance = DistanceService()

        self.database = DatabaseManager()

    def create_trip(

        self,

        departure,

        travel_date,

        destination,

        notes,

        vehicle
    ):

        weather_result = (

            self.weather.get_weather(

                destination

            )
        )

        distance_result = (

            self.distance.get_distance(

                departure,

                destination
            )
        )

        weather = None

        if weather_result["success"]:

            weather = (

                f'{weather_result["temperature"]}°C '

                f'({weather_result["condition"]})'
            )

        estimated_fare = None

        distance = None

        if distance_result["success"]:

            distance = (

                distance_result[
                    "distance"
                ]
            )

            fare_result = (

                self.fare.estimate_fare(

                    distance,

                    vehicle
                )
            )

            if fare_result["success"]:

                estimated_fare = (

                    fare_result[
                        "estimated_fare"
                    ]
                )

        trip = Trip(

            departure,

            travel_date,

            destination,

            notes,

            weather,

            estimated_fare
        )

        self.database.save_trip(
            trip
        )

        return trip

    def history(self):

        return (
            self.database
            .get_all_trips()
        )

    def delete_trip(
        self,
        trip_id
    ):

        self.database.delete_trip(
            trip_id
        )

    def clear_history(self):

        self.database.clear_history()