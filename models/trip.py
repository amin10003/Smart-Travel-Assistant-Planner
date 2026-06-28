class Trip:

    def __init__(

        self,

        departure,

        travel_date,

        destination,

        notes,

        weather=None,

        estimated_fare=None

    ):

        self.departure = departure

        self.travel_date = travel_date

        self.destination = destination

        self.notes = notes

        self.weather = weather

        self.estimated_fare = estimated_fare

    def display_trip(self):

        return (

            f"Departure: {self.departure}\n"

            f"Travel Date: {self.travel_date}\n"

            f"Final Destination: {self.destination}\n"

            f"Weather: {self.weather}\n"

            f"Estimated Fare: {self.estimated_fare}\n"

            f"Notes: {self.notes}"

        )