import sqlite3


class DatabaseManager:

    def __init__(self):

        self.connection = sqlite3.connect("database/travel.db")

        self.cursor = self.connection.cursor()

        self.create_table()

    def create_table(self):

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS travel_plan(

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                destination TEXT,

                travel_date TEXT,

                weather TEXT,

                estimated_fare REAL,

                notes TEXT
            )
            """)

        self.connection.commit()

    def save_trip(self, trip):

        self.cursor.execute(
            """
            INSERT INTO travel_plan(

                destination,

                travel_date,

                weather,

                estimated_fare,

                notes

            )

            VALUES (?, ?, ?, ?, ?)
            """,
            (
                trip.destination,
                trip.travel_date,
                trip.weather,
                trip.estimated_fare,
                trip.notes,
            ),
        )

        self.connection.commit()

    def get_all_trips(self):

        self.cursor.execute("""
            SELECT * FROM travel_plan
            """)

        return self.cursor.fetchall()

    def delete_trip(self, trip_id):

        self.cursor.execute(
            """
            DELETE FROM travel_plan
            WHERE id=?
            """,
            (trip_id,),
        )

        self.connection.commit()

    def clear_history(self):

        self.cursor.execute("""
        DELETE FROM travel_plan
        """)

        self.cursor.execute("""
        DELETE FROM sqlite_sequence
        WHERE name='travel_plan'
        """)

    

        self.connection.commit()
