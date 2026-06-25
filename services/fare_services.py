class FareService:

    def __init__(self):

        self.vehicle_rates = {
            "Bus": 30,
            "Van": 50,
            "Taxi": 150
        }

    def estimate_fare(
        self,
        distance,
        vehicle
    ):

        if vehicle not in self.vehicle_rates:

            return {
                "success": False,
                "message": "Vehicle not supported"
            }

        fare = (
            distance
            *
            self.vehicle_rates[
                vehicle
            ]
        )

        return {
            "success": True,
            "vehicle": vehicle,
            "distance": distance,
            "estimated_fare": fare
        }