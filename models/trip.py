class Trip:
    def __init__(self, destination, travel_date, notes, weather=None, estimated_fare=None):
        self.destination = destination
        self.travel_date = travel_date
        self.notes = notes
        self.weather = weather
        self.estimated_fare = estimated_fare

    def display_trip(self):
        return (
            f"Destination: {self.destination}\n"
            f"Travel Date: {self.travel_date}\n"
            f"Weather: {self.weather}\n"
            f"Estimated Fare: {self.estimated_fare}\n"
            f"Notes: {self.notes}"
        )


first_trip = Trip("Nairobi", "20/12/2026", "Carry jacket")

print(first_trip.display_trip())
