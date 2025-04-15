import sqlite3
import datetime

conn = sqlite3.connect("legal_case_tracker.db")
cursor = conn.cursor()

clients = [
    (1, "John Doe", "john@example.com"),
    (2, "Jane Smith", "jane@example.com")
]

today = datetime.date.today()
court_dates = [
    (1, 1, today + datetime.timedelta(days=2), "Settlement hearing"),
    (2, 2, today + datetime.timedelta(days=8), "Discovery deadline")
]

cursor.executemany("INSERT OR IGNORE INTO Clients VALUES (?, ?, ?)", clients)
cursor.executemany("INSERT OR IGNORE INTO CourtDates VALUES (?, ?, ?, ?)", court_dates)

conn.commit()
conn.close()
print("Sample data inserted.")
