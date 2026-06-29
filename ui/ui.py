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
            "1400x850"
        )

        self.window.configure(
            fg_color="#111827"
        )

        self.build_ui()

    def build_ui(self):

        title = ctk.CTkLabel(

            self.window,

            text="✈ Smart Travel Assistant",

            font=(

                "Arial",

                34,

                "bold"
            )
        )

        title.pack(
            pady=(20, 5)
        )

        subtitle = ctk.CTkLabel(

            self.window,

            text="Plan • Weather • Fare • History",

            text_color="gray"
        )

        subtitle.pack()

        main = ctk.CTkFrame(

            self.window,

            fg_color="transparent"
        )

        main.pack(

            fill="both",

            expand=True,

            padx=20,

            pady=20
        )

        left = ctk.CTkFrame(

            main,

            width=450,

            corner_radius=20
        )

        left.pack(

            side="left",

            fill="y",

            padx=(0, 15)
        )

        right = ctk.CTkFrame(

            main,

            corner_radius=20
        )

        right.pack(

            side="right",

            fill="both",

            expand=True
        )

        ctk.CTkLabel(

            left,

            text="Trip Operations",

            font=(
                "Arial",
                24,
                "bold"
            )

        ).pack(
            pady=20
        )

        self.departure = ctk.CTkEntry(

            left,

            placeholder_text="Departure Place",

            width=360,

            height=45
        )

        self.departure.pack(
            pady=8
        )

        self.destination = ctk.CTkEntry(

            left,

            placeholder_text="Final Destination",

            width=360,

            height=45
        )

        self.destination.pack(
            pady=8
        )

        self.date = ctk.CTkEntry(

            left,

            placeholder_text="Travel Date",

            width=360,

            height=45
        )

        self.date.pack(
            pady=8
        )

        ctk.CTkButton(

            left,

            text="📅 Select Date",

            width=200,

            command=self.open_calendar

        ).pack(
            pady=8
        )

        self.time = ctk.CTkEntry(

            left,

            placeholder_text="Time (HH:MM)",

            width=360,

            height=45
        )

        self.time.pack(
            pady=8
        )

        self.notes = ctk.CTkEntry(

            left,

            placeholder_text="Trip Notes",

            width=360,

            height=45
        )

        self.notes.pack(
            pady=8
        )

        self.vehicle = ctk.CTkOptionMenu(

            left,

            values=[
                "Bus",
                "Van",
                "Taxi"
            ],

            width=360,

            height=45
        )

        self.vehicle.pack(
            pady=8
        )

        self.trip_id = ctk.CTkEntry(

            left,

            placeholder_text="Trip ID To Delete",

            width=360,

            height=45
        )

        self.trip_id.pack(
            pady=8
        )

        ctk.CTkButton(

            left,

            text="Create Trip",

            height=45,

            command=self.create_trip

        ).pack(
            pady=8
        )

        ctk.CTkButton(

            left,

            text="Show History",

            height=45,

            command=self.show_history

        ).pack(
            pady=8
        )

        ctk.CTkButton(

            left,

            text="Delete Trip",

            height=45,

            command=self.delete_trip

        ).pack(
            pady=8
        )

        ctk.CTkButton(

            left,

            text="Clear All",

            height=45,

            fg_color="#c0392b",

            hover_color="#96281b",

            command=self.clear_history

        ).pack(
            pady=8
        )

        ctk.CTkLabel(

            right,

            text="Results & Trip History",

            font=(

                "Arial",

                24,

                "bold"
            )

        ).pack(
            pady=20
        )

        self.output = ctk.CTkTextbox(

            right,

            width=750,

            height=650,

            corner_radius=15
        )

        self.output.pack(

            fill="both",

            expand=True,

            padx=20,

            pady=10
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

Departure:
{row[1]}

Destination:
{row[2]}

Date:
{row[3]}

Weather:
{row[4]}

Fare:
KES {row[5]}

Notes:
{row[6]}

━━━━━━━━━━━━━━
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