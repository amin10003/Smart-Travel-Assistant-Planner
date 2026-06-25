import customtkinter as ctk

from planner import TravelPlanner


class TravelAssistantUI:

    def __init__(self):

        self.planner = TravelPlanner()

        self.window = ctk.CTk()

        self.window.title("Smart Travel Assistant")

        self.window.geometry("700x700")

        self.build_ui()

    def build_ui(self):

        title = ctk.CTkLabel(
            self.window, text="Smart Travel Assistant", font=("Arial", 26)
        )

        title.pack(pady=20)

        self.destination = ctk.CTkEntry(self.window, placeholder_text="Destination")

        self.destination.pack(pady=10)

        self.date = ctk.CTkEntry(self.window, placeholder_text="Travel Date")

        self.date.pack(pady=10)

        self.notes = ctk.CTkEntry(self.window, placeholder_text="Notes")

        self.notes.pack(pady=10)

        self.distance = ctk.CTkEntry(self.window, placeholder_text="Distance (km)")

        self.distance.pack(pady=10)

        self.vehicle = ctk.CTkOptionMenu(self.window, values=["Bus", "Van", "Taxi"])

        self.vehicle.pack(pady=10)

        save_button = ctk.CTkButton(
            self.window, text="Create Trip", command=self.create_trip
        )

        save_button.pack(pady=20)

        self.output = ctk.CTkTextbox(self.window, width=500, height=250)

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

            self.output.insert("end", trip.display_trip())

        except Exception as error:

            self.output.delete("1.0", "end")

            self.output.insert("end", str(error))

    def run(self):

        self.window.mainloop()
