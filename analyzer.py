"""
analyzer.py  –  ProductivityAnalyzer Class
CS1205 - Programming in Python

Concepts clearly demonstrated:
- OOP (class, constructor, methods)
- List, Dictionary, Set, Tuple
- map(), filter(), lambda
- datetime module
- Functions
"""

from datetime import date, timedelta
from collections import defaultdict


class ProductivityAnalyzer:
    """
    Analyzes a student's study sessions and produces insights.
    OOP Concept: Class with multiple methods.
    """

    # Tuple: fixed thresholds (immutable config values)
    THRESHOLDS: tuple = (
        2.0,
        4.0,
        0.6,
    )  # (min_daily_hrs, good_daily_hrs, balance_ratio)

    def __init__(self, sessions: list):
        """
        Constructor.
        sessions: List of dicts (from database)
        """
        self.sessions: list = sessions  # List concept
        # Derived collections computed once:
        self.subjects: set = set(s["subject"] for s in sessions)  # Set concept

    # ───────────────────────────────────────────────────────
    # Private helpers
    # ───────────────────────────────────────────────────────

    def _hours_by_subject(self) -> dict:
        """
        Aggregate total hours per subject.
        Concept: Dictionary
        """
        totals: dict = {}
        for s in self.sessions:
            totals[s["subject"]] = totals.get(s["subject"], 0) + s["hours"]
        return totals

    def _hours_by_date(self) -> dict:
        """Total hours per date.  Concept: Dictionary."""
        by_date: dict = defaultdict(float)
        for s in self.sessions:
            by_date[s["date"]] += s["hours"]
        return dict(by_date)

    # ───────────────────────────────────────────────────────
    # Dashboard stats
    # ───────────────────────────────────────────────────────

    def get_dashboard_stats(self) -> dict:
        """
        Compute summary statistics.
        Concepts: map(), filter(), lambda, Dictionary, List
        """
        if not self.sessions:
            return {
                "total_hours": 0,
                "total_sessions": 0,
                "avg_daily": 0,
                "most_studied": "—",
                "least_studied": "—",
                "avg_rating": 0,
                "productivity_score": 0,
                "unique_subjects": 0,
                "high_prod_count": 0,
            }

        # map() → extract hours from all sessions as a list
        all_hours: list = list(map(lambda s: s["hours"], self.sessions))
        total_hours: float = sum(all_hours)

        # filter() → sessions rated 4 or 5 (high productivity)
        high_prod = list(filter(lambda s: s["rating"] >= 4, self.sessions))

        # Average rating using map()
        ratings = list(map(lambda s: s["rating"], self.sessions))
        avg_rating = round(sum(ratings) / len(ratings), 1)

        # Subject totals (Dictionary)
        by_subject = self._hours_by_subject()

        # lambda for max/min subject
        most_studied = (
            max(by_subject, key=lambda k: by_subject[k]) if by_subject else "—"
        )
        least_studied = (
            min(by_subject, key=lambda k: by_subject[k]) if by_subject else "—"
        )

        # Average daily hours
        by_date = self._hours_by_date()
        avg_daily = round(total_hours / len(by_date), 1) if by_date else 0

        # Today's hours
        from datetime import timedelta

        today = date.today()
        today_iso = today.isoformat()
        hours_today = by_date.get(today_iso, 0)

        # Calculate current streak
        active_dates = set(d for d, hrs in by_date.items() if hrs > 0)
        current_streak = 0
        check_date = today

        # if today is not active, check if yesterday was active
        if check_date.isoformat() not in active_dates:
            yesterday = check_date - timedelta(days=1)
            if yesterday.isoformat() in active_dates:
                check_date = yesterday

        while check_date.isoformat() in active_dates:
            current_streak += 1
            check_date -= timedelta(days=1)

        # Productivity score: weighted  (map + lambda)
        productivity_score = (
            round(
                (
                    sum(map(lambda s: s["rating"] * s["hours"], self.sessions))
                    / total_hours
                )
                * 20,  # scale to 100
                1,
            )
            if total_hours
            else 0
        )

        return {
            "total_hours": round(total_hours, 1),
            "total_sessions": len(self.sessions),
            "avg_daily": avg_daily,
            "most_studied": most_studied,
            "least_studied": least_studied,
            "avg_rating": avg_rating,
            "productivity_score": min(productivity_score, 100),
            "unique_subjects": len(self.subjects),
            "high_prod_count": len(high_prod),
            "hours_today": hours_today,
            "current_streak": current_streak,
        }

    # ───────────────────────────────────────────────────────
    # Suggestions
    # ───────────────────────────────────────────────────────

    def get_suggestions(self) -> list:
        """
        Generate smart suggestions based on study patterns.
        Concept: Functions, if-else logic, List
        """
        suggestions: list = []
        if not self.sessions:
            suggestions.append(
                "Start adding study sessions to see your analytics!"
            )
            return suggestions

        by_date = self._hours_by_date()
        avg_daily = sum(by_date.values()) / len(by_date) if by_date else 0
        by_subject = self._hours_by_subject()
        total = sum(by_subject.values()) or 1

        min_hrs, good_hrs, balance_ratio = self.THRESHOLDS  # Tuple unpacking

        # Rule 1: Low study time
        if avg_daily < min_hrs:
            suggestions.append(
                f"⏰ Your average is {avg_daily:.1f}h/day. "
                "Aim for at least 2 hours daily for better performance."
            )

        # Rule 2: Subject imbalance (filter concept)
        dominant = list(
            filter(
                lambda item: item[1] / total > balance_ratio,
                by_subject.items(),
            )
        )
        if dominant:
            subj = dominant[0][0]
            suggestions.append(
                f"⚖️  '{subj}' takes up {dominant[0][1] / total * 100:.0f}% of your time. "  # noqa: E501
                "Balance your subjects for well-rounded performance."
            )

        # Rule 3: Great work
        if avg_daily >= good_hrs:
            suggestions.append(f"🌟 Excellent! You're averaging {
                    avg_daily:.1f}h/day. Keep it up!")

        # Rule 4: Low ratings
        ratings = list(map(lambda s: s["rating"], self.sessions))
        avg_r = sum(ratings) / len(ratings)
        if avg_r < 3:
            suggestions.append(
                "😴 Your productivity ratings are low. "
                "Try studying at a different time or in shorter, focused bursts."  # noqa: E501
            )

        # Rule 5: Consistency
        study_days = len(by_date)
        if study_days < 3:
            suggestions.append(
                "📅 Try to study more consistently — aim for at least 5 days a week."  # noqa: E501
            )

        return suggestions or [
            "✅ Looking great! Keep tracking your sessions."
        ]

    # ───────────────────────────────────────────────────────
    # Chart data
    # ───────────────────────────────────────────────────────

    def get_chart_data(self) -> dict:
        """
        Subject hours for bar chart.
        Concept: Dictionary, map()
        """
        by_subject = self._hours_by_subject()
        # map() to round values
        labels = list(by_subject.keys())
        values = list(map(lambda h: round(h, 1), by_subject.values()))
        return {"labels": labels, "values": values}

    def get_weekly_data(self) -> dict:
        """
        Last 7 days study hours.
        Concept: datetime, List, Dictionary
        """
        today = date.today()
        last7 = [
            (today - timedelta(days=i)).isoformat() for i in range(6, -1, -1)
        ]
        by_date = self._hours_by_date()

        labels = [d[5:] for d in last7]  # "MM-DD" format
        values = [round(by_date.get(d, 0), 1) for d in last7]

        return {"labels": labels, "values": values}

    def get_subject_analysis(self) -> list:
        """
        Per-subject detailed stats.
        Concept: filter(), Dictionary, List
        """
        analysis: list = []
        by_subject = self._hours_by_subject()
        total = sum(by_subject.values()) or 1

        for subj in self.subjects:
            # filter() to get only sessions for this subject
            subj_sessions = list(
                filter(lambda s: s["subject"] == subj, self.sessions)
            )
            # map() to extract ratings
            ratings = list(map(lambda s: s["rating"], subj_sessions))
            avg_r = round(sum(ratings) / len(ratings), 1) if ratings else 0
            hrs = round(by_subject[subj], 1)
            pct = round(hrs / total * 100, 1)
            analysis.append(
                {
                    "subject": subj,
                    "hours": hrs,
                    "sessions": len(subj_sessions),
                    "avg_rating": avg_r,
                    "percent": pct,
                }
            )

        # Sort by hours descending — lambda
        analysis.sort(key=lambda x: x["hours"], reverse=True)
        return analysis
