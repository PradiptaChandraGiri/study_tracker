"""
database.py  –  File Handling & Storage
CS1205 - Programming in Python

Concepts:
- File Handling (open, read, write, json)
- Exception Handling (try-except)
- Functions
- Dictionary, List
"""

import json
import os
from models import User, StudySession, MarkRecord

# ── File paths (Tuple: immutable config) ───────────────────
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_FILES: tuple = (
    os.path.join(BASE_DIR, "users.json"),
    os.path.join(BASE_DIR, "sessions.json"),
    os.path.join(BASE_DIR, "marks.json"),
)
USERS_FILE = DB_FILES[0]
SESSIONS_FILE = DB_FILES[1]
MARKS_FILE = DB_FILES[2]


# ═══════════════════════════════════════════════════════════
#  Initialization
# ═══════════════════════════════════════════════════════════
def init_db():
    """
    Create storage files if they don't exist.
    Concept: File handling — open(), write()
    """
    for filepath in DB_FILES:
        if not os.path.exists(filepath):
            try:
                with open(filepath, "w") as f:  # open() & write()
                    json.dump([], f)
            except IOError as e:
                print(f"Error creating {filepath}: {e}")


# ═══════════════════════════════════════════════════════════
#  Generic helpers
# ═══════════════════════════════════════════════════════════
def _read(filepath: str) -> list:
    """
    Read JSON file and return list.
    Concept: File handling — open(), read()
    Exception Handling: try-except
    """
    try:
        with open(filepath, "r") as f:  # open() & read()
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def _write(filepath: str, data: list):
    """
    Write list to JSON file.
    Concept: File handling — open(), write()
    """
    try:
        with open(filepath, "w") as f:  # open() & write()
            json.dump(data, f, indent=2)
    except IOError as e:
        raise RuntimeError(f"Write error: {e}")


# ═══════════════════════════════════════════════════════════
#  User operations
# ═══════════════════════════════════════════════════════════
def save_user(user: User):
    """Append a new user to storage.  Concept: List, file append."""
    users: list = _read(USERS_FILE)
    users.append(user.to_dict())  # List .append()
    _write(USERS_FILE, users)


def get_user_by_email(email: str) -> dict | None:
    """
    Find user dict by email.
    Concept: filter(), lambda
    """
    users: list = _read(USERS_FILE)
    # filter() with lambda
    result = list(filter(lambda u: u["email"] == email, users))
    return result[0] if result else None


def get_user_by_id(user_id: str) -> dict | None:
    """Find user dict by user_id."""
    users: list = _read(USERS_FILE)
    result = list(filter(lambda u: u["user_id"] == user_id, users))
    return result[0] if result else None


# ═══════════════════════════════════════════════════════════
#  Session operations
# ═══════════════════════════════════════════════════════════
def save_session(sess: StudySession):
    """
    Save a new study session.
    Concept: File handling, List
    """
    sessions: list = _read(SESSIONS_FILE)
    sessions.append(sess.to_dict())
    _write(SESSIONS_FILE, sessions)


def get_sessions(user_id: str) -> list:
    """
    Get all sessions for a user.
    Concept: filter(), lambda, List
    """
    all_sessions: list = _read(SESSIONS_FILE)
    # filter() — syllabus concept
    return list(filter(lambda s: s.get("user_id") == user_id, all_sessions))


def delete_session(user_id: str, session_id: str):
    """
    Delete a session by ID.
    Concept: filter(), lambda
    """
    all_sessions: list = _read(SESSIONS_FILE)
    # Keep all EXCEPT the one being deleted
    updated = list(
        filter(
            lambda s: (
                not (
                    s.get("session_id") == session_id
                    and s.get("user_id") == user_id
                )
            ),
            all_sessions,
        )
    )
    _write(SESSIONS_FILE, updated)


# ═══════════════════════════════════════════════════════════
#  Mark Operations (Academic Performance)
# ═══════════════════════════════════════════════════════════
def save_mark(mark: MarkRecord):
    """Save a new mark record."""
    marks: list = _read(MARKS_FILE)
    marks.append(mark.to_dict())
    _write(MARKS_FILE, marks)


def get_marks(user_id: str) -> list:
    """Get all marks for a user."""
    all_marks: list = _read(MARKS_FILE)
    return list(filter(lambda m: m.get("user_id") == user_id, all_marks))


def delete_mark(user_id: str, record_id: str):
    """Delete a mark by ID."""
    all_marks: list = _read(MARKS_FILE)
    updated = list(
        filter(
            lambda m: not (
                m.get("record_id") == record_id and m.get("user_id") == user_id
            ),
            all_marks,
        )
    )
    _write(MARKS_FILE, updated)
