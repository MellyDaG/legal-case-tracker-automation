cd legal-case-tracker-automation

import sqlite3

conn = sqlite3.connect("legal_case_tracker.db")
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Clients (
    client_id INTEGER PRIMARY KEY,
    client_name TEXT NOT NULL,
    email TEXT
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS CourtDates (
    court_id INTEGER PRIMARY KEY,
    client_id INTEGER,
    court_date DATE,
    description TEXT,
    FOREIGN KEY (client_id) REFERENCES Clients(client_id)
);
''')

conn.commit()
conn.close()
print("Database and tables created successfully.")
