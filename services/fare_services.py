class FareService:

    def __init__(self):

        self.vehicle_data = {
            "Bus": {"base": 80, "per_km": 15},
            "Van": {"base": 120, "per_km": 20},
            "Taxi": {"base": 250, "per_km": 35},
        }

        self.routes = {
            ("Nairobi", "Nakuru"): 160,
            ("Nairobi", "Mombasa"): 480,
            ("Nairobi", "Kisumu"): 350,
            ("Nakuru", "Eldoret"): 150,
            ("Garissa", "Nairobi"): 360,
            ("Mombasa", "Nairobi"): 400,
            ("Mandera", "Nairobi"): 600,
            ("Nairobi", "Eldoret"): 1700,
            ("Nairobi", "Kisii"): 1550,
            ("Nairobi", "Bungoma"): 1800,
            ("Nairobi", "Kakamega"): 1800,
            ("Nairobi", "Kitale"): 1850,
            ("Nairobi", "Busia"): 1950,
            ("Nairobi", "Siaya"): 1900,
            ("Nairobi", "Bondo"): 1900,
            ("Nairobi", "Migori"): 1600,
            ("Nairobi", "Homa Bay"): 1550,
            ("Nairobi", "Webuye"): 1800,
            ("Nairobi", "Mbale"): 1800,
            ("Nairobi", "Bomet"): 1700,
            ("Nairobi", "Keroka"): 1550,
            ("Nairobi", "Sori"): 1600,
            ("Nairobi", "Rongo"): 1700,
            ("Nairobi", "Kehancha"): 1600,
            ("Nairobi", "Sirare"): 1600,
            ("Nairobi", "Ndhiwa"): 1600,
            ("Nairobi", "Maseno"): 1900,
            ("Nairobi", "Kendu Bay"): 1550,
            ("Mombasa", "Busia"): 3000,
            ("Mombasa", "Kisumu"): 3000,
            ("Mombasa", "Maseno"): 3000,
            ("Kisumu", "Kisii"): 700,
            ("Kisii", "Nakuru"): 1000,
            ("Nakuru", "Kisumu"): 1500,
            ("Nakuru", "Kakamega"): 1550,
            ("Nakuru", "Kitale"): 1550,
            ("Nakuru", "Siaya"): 1550,
        }

    def estimate_fare(
        self, departure, destination, vehicle, rush_hour=False, rainy=False
    ):

        route = (departure, destination)

        if route not in self.routes:

            return {"success": False, "message": "Route unavailable"}

        distance = self.routes[route]

        vehicle_info = self.vehicle_data[vehicle]

        traffic = 1.5 if rush_hour else 1

        weather = 1.2 if rainy else 1

        fare = vehicle_info["base"] + (distance * vehicle_info["per_km"])

        fare = fare * traffic * weather

        return {"success": True, "distance": distance, "estimated_fare": round(fare, 2)}
