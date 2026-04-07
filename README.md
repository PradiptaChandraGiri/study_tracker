# Smart Study Tracker & Productivity Analyzer
### CS1205 – Programming in Python | College Project

---

## 🚀 How to Run

```bash
# 1. Create a virtual environment (recommended)
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
python app.py

# 4. Open browser
http://127.0.0.1:5000
```

---

## 📁 Project Structure

```
study_tracker/
├── app.py           ← Flask routes, session management
├── models.py        ← OOP: User & StudySession classes
├── analyzer.py      ← ProductivityAnalyzer class
├── database.py      ← File handling (JSON storage)
├── requirements.txt
├── users.json       ← auto-created on first run
├── sessions.json    ← auto-created on first run
├── templates/
│   ├── base.html
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── add_session.html
│   ├── history.html
│   ├── analytics.html
│   └── profile.html
└── static/
    ├── style.css
    └── script.js
```

---

## 📚 CS1205 Syllabus Concept Mapping

| Concept            | Location               | Description                                   |
|--------------------|------------------------|-----------------------------------------------|
| **Data Types**     | models.py              | str, float, int used in class attributes      |
| **List**           | analyzer.py, database.py | Study sessions stored and processed as lists|
| **Tuple**          | models.py, analyzer.py | RATING_LABELS, THRESHOLDS (immutable config)  |
| **Set**            | analyzer.py, app.py    | `self.subjects` — unique subject names        |
| **Dictionary**     | models.py, analyzer.py | `to_dict()`, `_hours_by_subject()`            |
| **Functions**      | analyzer.py            | `get_dashboard_stats()`, `get_suggestions()`  |
| **Lambda**         | analyzer.py, database.py | `lambda s: s["hours"]`, filter comparisons  |
| **map()**          | analyzer.py            | Extract hours, ratings from session lists     |
| **filter()**       | analyzer.py, database.py | Filter by subject, user_id, rating          |
| **Modules**        | app.py                 | flask, datetime, json, hashlib, os           |
| **File Handling**  | database.py            | open(), read(), write() with JSON             |
| **Exception Handling** | app.py, database.py | try-except in all routes and DB ops       |
| **Strings**        | models.py, templates   | .strip(), .title(), .lower(), f-strings      |
| **Date & Time**    | app.py, analyzer.py    | datetime, date.today(), timedelta             |
| **OOP – Classes**  | models.py, analyzer.py | User, StudySession, ProductivityAnalyzer      |
| **OOP – Objects**  | app.py                 | Instantiating User, StudySession objects      |
| **Constructor**    | models.py              | `__init__` in all three classes               |
| **Class Methods**  | models.py              | `from_dict()` classmethod                     |

---

## ✨ Features

- User registration & login with **password hashing** (SHA-256)
- Add study sessions (subject, hours, date, rating, notes, deadline)
- Dashboard with live stats cards
- Smart AI-style suggestions based on study patterns
- Deadline reminders with days-remaining countdown
- Study history with **filter by subject and date**
- Analytics with **Chart.js bar + line charts**
- Delete sessions
- Profile page with lifetime stats
- Mobile-responsive design

---

*Built for CS1205 Programming in Python*
