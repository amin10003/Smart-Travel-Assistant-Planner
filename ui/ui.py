import customtkinter as ctk

from planner import TravelPlanner


class TravelAssistantUI:

    def __init__(self):

        self.planner = TravelPlanner()

        self.window = ctk.CTk()

        self.window.title("Smart Travel Assistant")

        self.window.geometry("800x800")

        self.build_ui()

    def build_ui(self):

        title = ctk.CTkLabel(
            self.window, text="Smart Travel Assistant", font=("Arial", 28)
        )

        title.pack(pady=20)

        self.destination = ctk.CTkEntry(
            self.window, placeholder_text="Destination", width=250
        )

        self.destination.pack(pady=8)

        self.date = ctk.CTkEntry(self.window, placeholder_text="Travel Date", width=250)

        self.date.pack(pady=8)

        self.notes = ctk.CTkEntry(self.window, placeholder_text="Notes", width=250)

        self.notes.pack(pady=8)

        self.distance = ctk.CTkEntry(
            self.window, placeholder_text="Distance (km)", width=250
        )

        self.distance.pack(pady=8)

        self.vehicle = ctk.CTkOptionMenu(
            self.window, values=["Bus", "Van", "Taxi"], width=250
        )

        self.vehicle.pack(pady=10)

        create_button = ctk.CTkButton(
            self.window, text="Create Trip", command=self.create_trip
        )

        create_button.pack(pady=5)

        history_button = ctk.CTkButton(
            self.window, text="Show History", command=self.show_history
        )

        history_button.pack(pady=5)

        clear_button = ctk.CTkButton(
            self.window, text="Clear Plans", command=self.clear_history
        )

        clear_button.pack(pady=5)

        self.output = ctk.CTkTextbox(self.window, width=650, height=300)

        self.output.pack(pady=20)

    def create_trip(self):

        try:

            trip = self.planner.create_trip(
                self.destination.get(),
                self.date.get(),
                self.notes.get(),
                float(self.distance.get()),
                self.vehicle.get(),
            )

            self.output.delete("1.0", "end")

            self.output.insert("end", "Trip Created\n\n")

            self.output.insert("end", trip.display_trip())

        except Exception as error:

            self.output.delete("1.0", "end")

            self.output.insert("end", str(error))

    def show_history(self):

        trips = self.planner.history()

        self.output.delete("1.0", "end")

        if not trips:

            self.output.insert("end", "No saved trips.")

            return

        for row in trips:

            self.output.insert(
                "end",
                f"""
ID: {row[0]}
Destination: {row[1]}
Date: {row[2]}
Weather: {row[3]}
Fare: {row[4]}
Notes: {row[5]}

--------------------

""",
            )

    def clear_history(self):

        self.planner.clear_history()

        self.output.delete("1.0", "end")

        self.output.insert("end", "All plans deleted.")

    def run(self):

        self.window.mainloop()
