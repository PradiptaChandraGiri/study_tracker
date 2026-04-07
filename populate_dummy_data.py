import database as db
from models import User, StudySession, MarkRecord
from datetime import datetime, timedelta

def populate():
    db.init_db()

    email = "professor@demo.com"
    password = "password123"

    existing = db.get_user_by_email(email)
    if not existing:
        user = User(name="Professor Demo", email=email, password=password)
        db.save_user(user)
        u_id = user.user_id
    else:
        u_id = existing["user_id"]

    # Clear old sessions and marks for this user for a clean slate
    sessions = db.get_sessions(u_id)
    for s in sessions:
        db.delete_session(u_id, s["session_id"])
    
    marks = db.get_marks(u_id)
    for m in marks:
        db.delete_mark(u_id, m["record_id"])

    # Generate dates relative to today
    today = datetime.now()
    dates = [(today - timedelta(days=i)).strftime("%Y-%m-%d") for i in range(7, -1, -1)]
    future = (today + timedelta(days=10)).strftime("%Y-%m-%d")

    # Add realistic sessions
    new_sessions = [
        StudySession(u_id, "Computer Networks", 2.5, dates[0], 4, "Revised OSI Model", future),
        StudySession(u_id, "Database Systems", 3.0, dates[1], 5, "SQL Joins Practice", future),
        StudySession(u_id, "Web Development", 4.0, dates[2], 5, "Flask routing and templates", ""),
        StudySession(u_id, "Machine Learning", 2.0, dates[3], 3, "Linear Regression concepts", future),
        StudySession(u_id, "Computer Networks", 1.5, dates[4], 4, "TCP vs UDP", ""),
        StudySession(u_id, "Web Development", 3.5, dates[5], 5, "Built a Study Tracker UI", ""),
        StudySession(u_id, "Database Systems", 2.0, dates[6], 4, "Normal forms", future)
    ]
    
    for s in new_sessions:
        db.save_session(s)

    # Add realistic marks
    new_marks = [
        MarkRecord(u_id, "Computer Networks", 4, "38", "85"),
        MarkRecord(u_id, "Database Systems", 4, "42", "90"),
        MarkRecord(u_id, "Web Development", 4, "48", "95")
    ]
    
    for m in new_marks:
        db.save_mark(m)

    print("SUCCESS: Test data populated.")

if __name__ == "__main__":
    populate()
