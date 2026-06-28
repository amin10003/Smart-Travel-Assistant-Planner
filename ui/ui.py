import tkinter as tk
import customtkinter as ctk
from tkcalendar import Calendar

from planner import TravelPlanner


class TravelAssistantUI:

    def __init__(self):

        self.planner = TravelPlanner()

        self.window = ctk.CTk()

        self.window.title(
            "Smart Travel Assistant"
        )

        self.window.geometry(
            "800x850"
        )

        self.build_ui()

    def build_ui(self):

        title = ctk.CTkLabel(

            self.window,

            text="Smart Travel Assistant",

            font=("Arial", 28)

        )

        title.pack(
            pady=20
        )

        self.departure = ctk.CTkEntry(

            self.window,

            placeholder_text="Departure Place",

            width=300
        )

        self.departure.pack(
            pady=8
        )

        self.destination = ctk.CTkEntry(

            self.window,

            placeholder_text="Final Destination",

            width=300
        )

        self.destination.pack(
            pady=8
        )

        date_label = ctk.CTkLabel(

            self.window,

            text="Travel Date"
        )

        date_label.pack()

        self.date = ctk.CTkEntry(

            self.window,

            width=300
        )

        self.date.pack(
            pady=5
        )

        choose_button = ctk.CTkButton(

            self.window,

            text="Choose Date",

            command=self.open_calendar
        )

        choose_button.pack(
            pady=5
        )

        self.time = ctk.CTkEntry(

            self.window,

            placeholder_text="Time (HH:MM)",

            width=300
        )

        self.time.pack(
            pady=8
        )

        self.notes = ctk.CTkEntry(

            self.window,

            placeholder_text="Notes",

            width=300
        )

        self.notes.pack(
            pady=8
        )

        self.vehicle = ctk.CTkOptionMenu(

            self.window,

            values=[
                "Bus",
                "Van",
                "Taxi"
            ]
        )

        self.vehicle.pack(
            pady=10
        )

        self.trip_id = ctk.CTkEntry(

            self.window,

            placeholder_text="Trip ID to Delete",

            width=300
        )

        self.trip_id.pack(
            pady=8
        )

        ctk.CTkButton(

            self.window,

            text="Create Trip",

            command=self.create_trip

        ).pack(
            pady=5
        )

        ctk.CTkButton(

            self.window,

            text="Show History",

            command=self.show_history

        ).pack(
            pady=5
        )

        ctk.CTkButton(

            self.window,

            text="Delete One Trip",

            command=self.delete_trip

        ).pack(
            pady=5
        )

        ctk.CTkButton(

            self.window,

            text="Clear All Plans",

            command=self.clear_history

        ).pack(
            pady=5
        )

        self.output = ctk.CTkTextbox(

            self.window,

            width=650,

            height=300
        )

        self.output.pack(
            pady=20
        )

    def open_calendar(self):

        popup = tk.Toplevel(
            self.window
        )

        popup.title(
            "Select Date"
        )

        popup.resizable(
            False,
            False
        )

        width = 320
        height = 350

        self.window.update_idletasks()

        x = (
            self.window.winfo_x()
            +
            self.window.winfo_width() // 2
            -
            width // 2
        )

        y = (
            self.window.winfo_y()
            +
            self.window.winfo_height() // 2
            -
            height // 2
        )

        popup.geometry(
            f"{width}x{height}+{x}+{y}"
        )

        popup.transient(
            self.window
        )

        calendar = Calendar(

            popup,

            selectmode="day",

            date_pattern="yyyy-mm-dd"
        )

        calendar.pack(

            expand=True,

            fill="both",

            padx=10,

            pady=10
        )

        def save_date():

            self.date.delete(
                0,
                "end"
            )

            self.date.insert(
                0,
                calendar.get_date()
            )

            popup.destroy()

        ctk.CTkButton(

            popup,

            text="Select",

            command=save_date

        ).pack(
            pady=10
        )

    def clear_inputs(self):

        self.departure.delete(
            0,
            "end"
        )

        self.destination.delete(
            0,
            "end"
        )

        self.date.delete(
            0,
            "end"
        )

        self.time.delete(
            0,
            "end"
        )

        self.notes.delete(
            0,
            "end"
        )

    def create_trip(self):

        try:

            trip = self.planner.create_trip(

                self.departure.get(),

                f"{self.date.get()} {self.time.get()}",

                self.destination.get(),

                self.notes.get(),

                self.vehicle.get()
            )

            self.output.delete(
                "1.0",
                "end"
            )

            self.output.insert(
                "end",
                trip.display_trip()
            )

            self.clear_inputs()

        except Exception as error:

            self.output.delete(
                "1.0",
                "end"
            )

            self.output.insert(
                "end",
                str(error)
            )

    def show_history(self):

        trips = self.planner.history()

        self.output.delete(
            "1.0",
            "end"
        )

        for row in trips:

            self.output.insert(

                "end",

                f"""
ID: {row[0]}
Departure: {row[1]}
Destination: {row[2]}
Date: {row[3]}
Weather: {row[4]}
Fare: {row[5]}
Notes: {row[6]}

--------------------
"""
            )

    def delete_trip(self):

        try:

            self.planner.delete_trip(

                int(
                    self.trip_id.get()
                )
            )

            self.trip_id.delete(
                0,
                "end"
            )

            self.show_history()

        except:

            self.output.delete(
                "1.0",
                "end"
            )

            self.output.insert(
                "end",
                "Enter valid Trip ID"
            )

    def clear_history(self):

        self.planner.clear_history()

        self.output.delete(
            "1.0",
            "end"
        )

        self.output.insert(
            "end",
            "All plans deleted."
        )

    def run(self):

        self.window.mainloop()