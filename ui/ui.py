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

        self.build_ui()

    def build_ui(self):

        container = ctk.CTkFrame(

            self.window,

            corner_radius=20
        )

        container.pack(

            padx=30,

            pady=30,

            fill="both",

            expand=True
        )

        title = ctk.CTkLabel(

            container,

            text="✈ Smart Travel Assistant",

            font=(
                "Arial",
                32,
                "bold"
            )
        )

        title.pack(
            pady=(25, 10)
        )

        subtitle = ctk.CTkLabel(

            container,

            text="Plan trips and estimate fare",

            text_color="gray"
        )

        subtitle.pack(
            pady=(0, 20)
        )

        self.departure = ctk.CTkEntry(

            container,

            placeholder_text="Departure Place",

            width=400,

            height=45
        )

        self.departure.pack(
            pady=8
        )

        self.destination = ctk.CTkEntry(

            container,

            placeholder_text="Final Destination",

            width=400,

            height=45
        )

        self.destination.pack(
            pady=8
        )

        self.date = ctk.CTkEntry(

            container,

            placeholder_text="Travel Date",

            width=400,

            height=45
        )

        self.date.pack(
            pady=8
        )

        ctk.CTkButton(

            container,

            text="📅 Choose Date",

            width=250,

            height=40,

            command=self.open_calendar

        ).pack(
            pady=8
        )

        self.time = ctk.CTkEntry(

            container,

            placeholder_text="Time (HH:MM)",

            width=400,

            height=45
        )

        self.time.pack(
            pady=8
        )

        self.notes = ctk.CTkEntry(

            container,

            placeholder_text="Trip Notes",

            width=400,

            height=45
        )

        self.notes.pack(
            pady=8
        )

        self.vehicle = ctk.CTkOptionMenu(

            container,

            width=400,

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

            container,

            placeholder_text="Trip ID to Delete",

            width=400,

            height=45
        )

        self.trip_id.pack(
            pady=8
        )

        button_frame = ctk.CTkFrame(

            container,

            fg_color="transparent"
        )

        button_frame.pack(
            pady=10
        )

        ctk.CTkButton(

            button_frame,

            text="Create",

            width=150,

            command=self.create_trip

        ).grid(
            row=0,
            column=0,
            padx=5
        )

        ctk.CTkButton(

            button_frame,

            text="History",

            width=150,

            command=self.show_history

        ).grid(
            row=0,
            column=1,
            padx=5
        )

        ctk.CTkButton(

            button_frame,

            text="Delete",

            width=150,

            command=self.delete_trip

        ).grid(
            row=1,
            column=0,
            pady=10
        )

        ctk.CTkButton(

            button_frame,

            text="Clear All",

            width=150,

            command=self.clear_history

        ).grid(
            row=1,
            column=1
        )

        self.output = ctk.CTkTextbox(

            container,

            width=760,

            height=240,

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

        self.window.update()

        x = (
            self.window.winfo_x()
            +
            (
                self.window.winfo_width()
                // 2
            )
            -
            (
                width
                // 2
            )
        )

        y = (
            self.window.winfo_y()
            +
            (
                self.window.winfo_height()
                // 2
            )
            -
            (
                height
                // 2
            )
        )

        popup.geometry(
            f"{width}x{height}+{x}+{y}"
        )

        popup.title(
            "Choose Date"
        )

        calendar = Calendar(

            popup,

            date_pattern="yyyy-mm-dd"
        )

        calendar.pack(

            expand=True,

            fill="both",

            padx=10,

            pady=10
        )

        def save():

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

            command=save

        ).pack(
            pady=10
        )

    def clear_inputs(self):

        self.departure.delete(0, "end")

        self.destination.delete(0, "end")

        self.date.delete(0, "end")

        self.time.delete(0, "end")

        self.notes.delete(0, "end")

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

        self.output.delete(
            "1.0",
            "end"
        )

        for row in self.planner.history():

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

────────────────
"""
            )

    def delete_trip(self):

        try:

            self.planner.delete_trip(
                int(
                    self.trip_id.get()
                )
            )

            self.show_history()

        except:

            self.output.insert(
                "end",
                "\nInvalid Trip ID"
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