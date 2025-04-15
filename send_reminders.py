import sqlite3
import datetime
import smtplib
from email.mime.text import MIMEText

EMAIL_ADDRESS = "your_email@gmail.com"
EMAIL_PASSWORD = "your_password"

def send_email(to_email, subject, body):
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = to_email

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)

def main():
    conn = sqlite3.connect("legal_case_tracker.db")
    cursor = conn.cursor()

    today = datetime.date.today()
    upcoming = today + datetime.timedelta(days=7)

    cursor.execute('''
    SELECT c.client_name, c.email, cd.court_date, cd.description
    FROM Clients c
    JOIN CourtDates cd ON c.client_id = cd.client_id
    WHERE cd.court_date BETWEEN ? AND ?
    ''', (today, upcoming))

    results = cursor.fetchall()

    for name, email, date, description in results:
        body = f"""Hello {name},

This is a reminder for your upcoming court date:

📅 Date: {date}
📌 Purpose: {description}

Please ensure you’re prepared.

- Legal Team"""
        send_email(email, "📢 Court Date Reminder", body)

    print("Reminders sent.")
    conn.close()

if __name__ == "__main__":
    main()
