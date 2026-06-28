class FareService:

    def __init__(self):

        self.vehicle_config = {

            "Bus": {
                "base": 100,
                "per_km": 20
            },

            "Van": {
                "base": 150,
                "per_km": 30
            },

            "Taxi": {
                "base": 300,
                "per_km": 50
            }
        }

    def estimate_fare(

        self,

        distance,

        vehicle,

        traffic=1.0,

        weather=1.0
    ):

        if vehicle not in self.vehicle_config:

            return {

                "success": False,

                "message":
                "Vehicle not supported"
            }

        config = (

            self
            .vehicle_config[
                vehicle
            ]
        )

        fare = (

            config["base"]

            +

            (
                distance
                *
                config["per_km"]
            )

        )

        fare = (

            fare
            *
            traffic
            *
            weather
        )

        return {

            "success": True,

            "distance": distance,

            "vehicle": vehicle,

            "estimated_fare": round(
                fare,
                2
            )
        }