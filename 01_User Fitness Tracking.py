import sqlite3
import datetime

class GymUser:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.database = "database/fitness_tracker.db"
        self.create_table()

    def create_table(self):
        conn = sqlite3.connect(self.database)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS user_data (
                id INTEGER PRIMARY KEY,
                name TEXT,
                date TEXT,
                weight REAL,
                calories INT,
                workout TEXT,
                burned_calories INT
            )
        """)
        conn.commit()
        conn.close()

    def log_progress(self, weight, calories, workout, burned_calories):
        conn = sqlite3.connect(self.database)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO user_data (name, date, weight, calories, workout, burned_calories)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (self.name, datetime.date.today(), weight, calories, workout, burned_calories))
        conn.commit()
        conn.close()
        print("Progress logged successfully!")

    def get_progress(self):
        conn = sqlite3.connect(self.database)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM user_data WHERE name = ?", (self.name,))
        records = cursor.fetchall()
        conn.close()
        return records