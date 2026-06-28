import tkinter as tk
import customtkinter as ctk
from tkcalendar import Calendar

from planner import TravelPlanner


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class TravelAssistantUI:

    def __init__(self):

        self.planner = TravelPlanner()

        self.window = ctk.CTk()

        self.window.title(
            "Smart Travel Assistant"
        )

        self.window.geometry(
            "900x900"
        )

        self.window.configure(
            fg_color="#151821"
        )

        self.build_ui()

    def build_ui(self):

        self.card = ctk.CTkFrame(

            self.window,

            width=720,

            corner_radius=20
        )

        self.card.pack(

            pady=30,

            padx=30,

            fill="both",

            expand=True
        )

        title = ctk.CTkLabel(

            self.card,

            text="✈ Smart Travel Assistant",

            font=(
                "Arial",
                34,
                "bold"
            )
        )

        title.pack(
            pady=(30, 10)
        )

        subtitle = ctk.CTkLabel(

            self.card,

            text="Plan trips • Check weather • Estimate fare",

            text_color="gray"
        )

        subtitle.pack(
            pady=(0, 25)
        )

        self.departure = ctk.CTkEntry(

            self.card,

            placeholder_text="Departure Place",

            width=450,

            height=45
        )

        self.departure.pack(
            pady=8
        )

        self.destination = ctk.CTkEntry(

            self.card,

            placeholder_text="Final Destination",

            width=450,

            height=45
        )

        self.destination.pack(
            pady=8
        )

        self.date = ctk.CTkEntry(

            self.card,

            placeholder_text="Travel Date",

            width=450,

            height=45
        )

        self.date.pack(
            pady=8
        )

        ctk.CTkButton(

            self.card,

            text="📅 Choose Date",

            width=220,

            height=40,

            command=self.open_calendar

        ).pack(
            pady=8
        )

        self.time = ctk.CTkEntry(

            self.card,

            placeholder_text="Time (HH:MM)",

            width=450,

            height=45
        )

        self.time.pack(
            pady=8
        )

        self.notes = ctk.CTkEntry(

            self.card,

            placeholder_text="Trip Notes",

            width=450,

            height=45
        )

        self.notes.pack(
            pady=8
        )

        self.vehicle = ctk.CTkOptionMenu(

            self.card,

            width=450,

            height=45,

            values=[
                "Bus",
                "Van",
                "Taxi"
            ]
        )

        self.vehicle.pack(
            pady=8
        )

        self.trip_id = ctk.CTkEntry(

            self.card,

            placeholder_text="Trip ID to Delete",

            width=450,

            height=45
        )

        self.trip_id.pack(
            pady=8
        )

        button_frame = ctk.CTkFrame(

            self.card,

            fg_color="transparent"
        )

        button_frame.pack(
            pady=20
        )

        ctk.CTkButton(

            button_frame,

            text="Create",

            width=150,

            command=self.create_trip

        ).grid(
            row=0,
            column=0,
            padx=8
        )

        ctk.CTkButton(

            button_frame,

            text="History",

            width=150,

            command=self.show_history

        ).grid(
            row=0,
            column=1,
            padx=8
        )

        ctk.CTkButton(

            button_frame,

            text="Delete",

            width=150,

            command=self.delete_trip

        ).grid(
            row=0,
            column=2,
            padx=8
        )

        ctk.CTkButton(

            button_frame,

            text="Clear",

            width=150,

            command=self.clear_history

        ).grid(
            row=0,
            column=3,
            padx=8
        )

        self.output = ctk.CTkTextbox(

            self.card,

            width=700,

            height=220,

            corner_radius=15
        )

        self.output.pack(
            pady=20
        )

    def open_calendar(self):

        popup = tk.Toplevel(
            self.window
        )

        width = 320
        height = 350

        self.window.update_idletasks()

        x = (
            self.window.winfo_x()
            + self.window.winfo_width() // 2
            - width // 2
        )

        y = (
            self.window.winfo_y()
            + self.window.winfo_height() // 2
            - height // 2
        )

        popup.geometry(
            f"{width}x{height}+{x}+{y}"
        )

        calendar = Calendar(

            popup,

            selectmode="day",

            date_pattern="yyyy-mm-dd"
        )

        calendar.pack(
            fill="both",
            expand=True
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

        for field in [

            self.departure,

            self.destination,

            self.date,

            self.time,

            self.notes

        ]:

            field.delete(
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

────────────────────
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