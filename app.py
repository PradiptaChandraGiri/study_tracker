"""
Smart Study Tracker & Productivity Analyzer
Main Flask Application
CS1205 - Programming in Python

Concepts used:
- Modules (Flask, datetime, json, hashlib, os)
- Functions
- Exception Handling
- Session management
- File Handling
"""

from ui_templates import templates_dict
from jinja2 import DictLoader
from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    session,
    jsonify,
)
from models import User, StudySession, MarkRecord
from analyzer import ProductivityAnalyzer
import database as db
import json
from datetime import datetime, date
from dotenv import load_dotenv
import ai_service

load_dotenv()

# ── App setup ──────────────────────────────────────────────
app = Flask(__name__)
app.secret_key = "study_tracker_secret_2024"  # Tuple-like fixed config value

app.jinja_loader = DictLoader(templates_dict)


# ── Helper: login guard ─────────────────────────────────────
def login_required(f):
    """Decorator: redirect to login if not authenticated."""
    from functools import wraps

    @wraps(f)
    def decorated(*args, **kwargs):
        if "user_id" not in session:
            return redirect(url_for("login"))
        return f(*args, **kwargs)

    return decorated


# ═══════════════════════════════════════════════════════════
#  AUTH ROUTES
# ═══════════════════════════════════════════════════════════


@app.route("/")
def index():
    if "user_id" in session:
        return redirect(url_for("dashboard"))
    return redirect(url_for("login"))


@app.route("/register", methods=["GET", "POST"])
def register():
    error = None
    if request.method == "POST":
        try:
            name = request.form["name"].strip()
            email = request.form["email"].strip().lower()
            password = request.form["password"]
            if not name or not email or not password:
                raise ValueError("All fields are required.")
            if len(password) < 6:
                raise ValueError("Password must be at least 6 characters.")
            if db.get_user_by_email(email):
                raise ValueError("Email already registered.")
            user = User(name=name, email=email, password=password)
            db.save_user(user)
            return redirect(url_for("login"))
        except ValueError as e:
            error = str(e)
        except Exception:
            error = "Registration failed. Please try again."
    return render_template("register.html", error=error)


@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        try:
            email = request.form["email"].strip().lower()
            password = request.form["password"]
            user_data = db.get_user_by_email(email)
            if not user_data:
                raise ValueError("No account found with that email.")
            user = User.from_dict(user_data)
            if not user.check_password(password):
                raise ValueError("Incorrect password.")
            session["user_id"] = user.user_id
            session["user_name"] = user.name
            return redirect(url_for("dashboard"))
        except ValueError as e:
            error = str(e)
        except Exception:
            error = "Login failed. Please try again."
    return render_template("login.html", error=error)


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


@app.route("/privacy")
def privacy():
    return render_template("privacy.html")


# ═══════════════════════════════════════════════════════════
#  MAIN PAGES
# ═══════════════════════════════════════════════════════════


@app.route("/dashboard")
@login_required
def dashboard():
    """
    Dashboard: fetch all sessions and compute summary stats.
    Concept: Dictionary, List comprehension, map()
    """
    user_id = session["user_id"]
    sessions = db.get_sessions(user_id)  # List of dicts

    analyzer = ProductivityAnalyzer(sessions)
    stats = analyzer.get_dashboard_stats()  # Dictionary
    suggestions = analyzer.get_suggestions()  # List of strings

    return render_template(
        "dashboard.html",
        stats=stats,
        suggestions=suggestions,
        user_name=session["user_name"],
    )


@app.route("/timer", methods=["GET"])
@login_required
def timer():
    user_id = session["user_id"]
    sessions = db.get_sessions(user_id)
    # Get unique recent subjects
    recent_subjects = list(set([s["subject"] for s in sessions]))
    return render_template("timer.html", subjects=recent_subjects)


@app.route("/add_session", methods=["GET", "POST"])
@login_required
def add_session():
    """
    Add a new study session.
    Concept: OOP (StudySession class), Exception handling
    """
    error = None
    success = None
    if request.method == "POST":
        try:
            subject = request.form["subject"].strip()
            hours_str = request.form["hours"]
            date_str = request.form["date"]
            rating_str = request.form["rating"]
            notes = request.form.get("notes", "").strip()
            deadline = request.form.get("deadline", "").strip()

            if not subject:
                raise ValueError("Subject is required.")

            hours = float(hours_str)
            rating = int(rating_str)
            if hours <= 0 or hours > 24:
                raise ValueError("Hours must be between 0 and 24.")
            if rating < 1 or rating > 5:
                raise ValueError("Rating must be between 1 and 5.")

            sess = StudySession(
                user_id=session["user_id"],
                subject=subject,
                hours=hours,
                date=date_str,
                rating=rating,
                notes=notes,
                deadline=deadline,
            )
            db.save_session(sess)
            success = "Session added successfully!"
        except ValueError as e:
            error = str(e)
        except Exception:
            error = "Could not save session. Please try again."

    today = date.today().isoformat()
    return render_template(
        "add_session.html", error=error, success=success, today=today
    )
@app.route("/forest")
@login_required
def forest():
    """
    Renders the Forest gamification page.
    """
    user_id = session["user_id"]
    sessions = db.get_sessions(user_id)
    tree_count = len(sessions)
    total_hours = sum(s.get("hours", 0) for s in sessions)
    return render_template("forest.html", tree_count=tree_count, total_hours=round(total_hours, 2))


@app.route("/history")
@login_required
def history():
    """
    Study history with filter support.
    Concept: filter(), lambda
    """
    user_id = session["user_id"]
    all_sess = db.get_sessions(user_id)  # List

    # Collect unique subjects for filter dropdown  — Set concept
    subjects: set = set(s["subject"] for s in all_sess)

    # Query filters
    filter_subject = request.args.get("subject", "")
    filter_date = request.args.get("date", "")

    # filter() with lambda  — syllabus concept
    filtered = list(
        filter(
            lambda s: (
                (filter_subject == "" or s["subject"] == filter_subject)
                and (filter_date == "" or s["date"] == filter_date)
            ),
            all_sess,
        )
    )

    # Sort most-recent first
    filtered.sort(key=lambda s: s["date"], reverse=True)

    return render_template(
        "history.html",
        sessions=filtered,
        subjects=sorted(subjects),
        filter_subject=filter_subject,
        filter_date=filter_date,
    )


@app.route("/analytics")
@login_required
def analytics():
    """
    Analytics page with chart data.
    Concept: map(), Dictionary, Analyzer class
    """
    user_id = session["user_id"]
    sessions = db.get_sessions(user_id)
    analyzer = ProductivityAnalyzer(sessions)

    chart_data = analyzer.get_chart_data()
    weekly_data = analyzer.get_weekly_data()
    subject_stats = analyzer.get_subject_analysis()

    return render_template(
        "analytics.html",
        chart_data=json.dumps(chart_data),
        weekly_data=json.dumps(weekly_data),
        subject_stats=subject_stats,
    )


@app.route("/academic", methods=["GET", "POST"])
@login_required
def academic():
    """Manage Mid-Sem marks and compute End-Sem goals."""
    error = None
    success = None
    user_id = session["user_id"]

    if request.method == "POST":
        try:
            subject = request.form["subject"]
            semester = request.form["semester"]
            mid_sem = request.form["mid_sem"]
            target = request.form["target"]

            mark = MarkRecord(user_id, subject, semester, mid_sem, target)
            db.save_mark(mark)
            success = "Marks captured! Check your end-sem strategy."
        except Exception as e:
            error = str(e) or "Could not save marks."

    # Load and map dictionaries back to MarkRecord objects
    raw_marks = db.get_marks(user_id)
    marks = [MarkRecord.from_dict(m) for m in raw_marks]

    return render_template(
        "academic.html", marks=marks, error=error, success=success
    )


@app.route("/profile")
@login_required
def profile():
    user_data = db.get_user_by_id(session["user_id"])
    if not user_data:
        session.clear()
        return redirect(url_for("login"))
    sessions = db.get_sessions(session["user_id"])
    analyzer = ProductivityAnalyzer(sessions)
    stats = analyzer.get_dashboard_stats()
    joined = user_data.get("joined", "N/A")
    return render_template(
        "profile.html", user=user_data, stats=stats, joined=joined
    )


# ═══════════════════════════════════════════════════════════
#  API endpoints (used by JS for search / delete)
# ═══════════════════════════════════════════════════════════


@app.route("/api/ai_suggestions")
@login_required
def api_ai_suggestions():
    from analyzer import ProductivityAnalyzer

    sessions = db.get_sessions(session["user_id"])
    analyzer = ProductivityAnalyzer(sessions)
    stats = analyzer.get_dashboard_stats()
    suggestions = ai_service.generate_smart_suggestions(stats)
    return jsonify({"suggestions": suggestions})


@app.route("/api/chat", methods=["POST"])
@login_required
def api_chat():
    data = request.get_json() or {}
    messages = data.get("messages", [])
    marks = db.get_marks(session["user_id"])
    response_text = ai_service.chat_with_bot(
        messages, session.get("user_name", "Student"), marks_data=marks
    )
    return jsonify({"reply": response_text})


@app.route("/api/delete_session/<session_id>", methods=["DELETE"])
@login_required
def delete_session(session_id):
    try:
        db.delete_session(session["user_id"], session_id)
        return jsonify({"status": "ok"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})


@app.route("/api/delete_mark/<record_id>", methods=["DELETE"])
@login_required
def delete_mark(record_id):
    try:
        db.delete_mark(session["user_id"], record_id)
        return jsonify({"status": "ok"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


@app.route("/api/deadlines")
@login_required
def api_deadlines():
    """Return upcoming deadlines with days_remaining.  Concept: datetime"""
    sessions = db.get_sessions(session["user_id"])
    today = date.today()
    deadlines = []
    seen = set()
    for s in sessions:
        dl = s.get("deadline", "")
        key = (s.get("subject", ""), dl)
        if dl and key not in seen:
            seen.add(key)
            try:
                dl_date = datetime.strptime(dl, "%Y-%m-%d").date()
                days = (dl_date - today).days
                deadlines.append(
                    {"subject": s["subject"], "deadline": dl, "days": days}
                )
            except ValueError:
                pass
    deadlines.sort(key=lambda x: x["days"])
    return jsonify(deadlines)


@app.route("/save-session", methods=["POST"])
@login_required
def save_session():
    data = request.get_json()
    if not data:
        return jsonify({"status": "error", "message": "No data provided"}), 400
    
    subject = data.get("subject", "Focus Session")
    hours = float(data.get("hours", 0))
    
    try:
        sess = StudySession(
            user_id=session["user_id"],
            subject=subject,
            hours=hours,
            date=date.today().isoformat(),
            rating=5,
            notes="Focus Timer Session",
            deadline=""
        )
        db.save_session(sess)
        return jsonify({"status": "saved"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


if __name__ == "__main__":
    db.init_db()
    app.run(debug=True, port=5000, ssl_context="adhoc")
