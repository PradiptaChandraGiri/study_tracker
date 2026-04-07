"""
models.py  –  OOP Classes for Smart Study Tracker
CS1205 - Programming in Python

Concepts used:
- Classes & Objects
- Constructor (__init__)
- Class methods
- Data Types (str, float, int)
- Modules (hashlib, uuid, datetime)
"""

import hashlib
import uuid
from datetime import datetime


# ═══════════════════════════════════════════════════════════
#  User Class
# ═══════════════════════════════════════════════════════════
class User:
    """
    Represents a registered student user.
    OOP Concept: Class with constructor and methods.
    """

    def __init__(
        self, name: str, email: str, password: str, user_id: str = None
    ):
        # Constructor sets instance attributes (data types: str)
        self.user_id = user_id or str(uuid.uuid4())[:8]
        self.name = name
        self.email = email
        self.password = self._hash_password(password)  # Hashed (str)
        self.joined = datetime.now().strftime("%Y-%m-%d")  # date module

    # ── Password hashing ──────────────────────────────────
    def _hash_password(self, raw: str) -> str:
        """Hash password using SHA-256.  Security concept."""
        return hashlib.sha256(raw.encode()).hexdigest()

    def check_password(self, raw: str) -> bool:
        """Verify a plain password against stored hash."""
        return self._hash_password(raw) == self.password

    # ── Serialization ─────────────────────────────────────
    def to_dict(self) -> dict:
        """Convert to dictionary for JSON storage.  Dict concept."""
        return {
            "user_id": self.user_id,
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "joined": self.joined,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "User":
        """
        Create a User from a dictionary.
        Class method concept.
        """
        obj = cls.__new__(cls)
        obj.user_id = data["user_id"]
        obj.name = data["name"]
        obj.email = data["email"]
        obj.password = data["password"]  # already hashed
        obj.joined = data.get("joined", "")
        return obj


# ═══════════════════════════════════════════════════════════
#  StudySession Class
# ═══════════════════════════════════════════════════════════
class StudySession:
    """
    Represents a single study session logged by the student.
    OOP Concept: Class, constructor, method, instance attributes.

    Attributes use multiple data types:
        subject  → str
        hours    → float
        date     → str  (YYYY-MM-DD)
        rating   → int  (1-5)
        notes    → str
        deadline → str  (YYYY-MM-DD, optional)
    """

    # Tuple: fixed rating labels (immutable config)
    RATING_LABELS: tuple = (
        "",
        "Very Low",
        "Low",
        "Average",
        "High",
        "Excellent",
    )

    def __init__(
        self,
        user_id: str,
        subject: str,
        hours: float,
        date: str,
        rating: int,
        notes: str = "",
        deadline: str = "",
        session_id: str = None,
    ):
        self.session_id = session_id or str(uuid.uuid4())[:10]
        self.user_id = user_id
        self.subject = subject.strip().title()
        self.hours = float(hours)
        self.date = date
        self.rating = int(rating)
        self.notes = notes
        self.deadline = deadline

    @property
    def rating_label(self) -> str:
        """Return human-readable label for rating."""
        return self.RATING_LABELS[self.rating]

    def to_dict(self) -> dict:
        """Serialize to dictionary.  Dict concept."""
        return {
            "session_id": self.session_id,
            "user_id": self.user_id,
            "subject": self.subject,
            "hours": self.hours,
            "date": self.date,
            "rating": self.rating,
            "notes": self.notes,
            "deadline": self.deadline,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "StudySession":
        return cls(
            user_id=data["user_id"],
            subject=data["subject"],
            hours=data["hours"],
            date=data["date"],
            rating=data["rating"],
            notes=data.get("notes", ""),
            deadline=data.get("deadline", ""),
            session_id=data.get("session_id"),
        )

    def __repr__(self) -> str:
        return f"<StudySession {self.subject} | {self.hours}h | {self.date}>"


# ═══════════════════════════════════════════════════════════
#  MarkRecord Class (Mid-Sem to End-Sem Strategy)
# ═══════════════════════════════════════════════════════════
class MarkRecord:
    """
    Represents a student's academic marks for a specific subject in a semester.
    Includes logic to predict required end-sem marks.
    """

    def __init__(
        self,
        user_id: str,
        subject: str,
        semester: int,
        mid_sem_score: float,
        target_grade: str,
        record_id: str = None,
    ):
        self.record_id = record_id or str(uuid.uuid4())[:10]
        self.user_id = user_id
        self.subject = subject.strip().title()
        self.semester = int(semester)
        self.mid_sem_score = float(mid_sem_score)  # Assumed out of 30
        self.target_grade = target_grade.strip().upper()

    @property
    def target_total(self) -> int:
        """Map a letter grade to a total out of 100."""
        targets = {"O": 90, "A+": 85, "A": 80, "B": 70, "C": 60, "PASS": 40}
        return targets.get(self.target_grade, 40)

    @property
    def required_end_sem(self) -> float:
        """
        Calculate required end-sem marks (out of 60).
        Total marks = Mid-Sem (30) + End-Sem (60) + Internals (10).
        Assuming average internals of 8/10 for simple math.
        """
        needed = self.target_total - self.mid_sem_score - 8
        if needed > 60:
            return 999.0  # Impossible
        return max(0.0, round(needed, 1))

    def to_dict(self) -> dict:
        return {
            "record_id": self.record_id,
            "user_id": self.user_id,
            "subject": self.subject,
            "semester": self.semester,
            "mid_sem_score": self.mid_sem_score,
            "target_grade": self.target_grade,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "MarkRecord":
        return cls(
            user_id=data["user_id"],
            subject=data["subject"],
            semester=data["semester"],
            mid_sem_score=data["mid_sem_score"],
            target_grade=data["target_grade"],
            record_id=data.get("record_id"),
        )
