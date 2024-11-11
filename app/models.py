from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Goal(db.Model):
    __tablename__ = 'company_goals'
    
    id = db.Column(db.Integer, primary_key=True)
    department = db.Column(db.String(100), nullable=False)
    statement = db.Column(db.Text, nullable=False)
    success_criteria = db.Column(db.Text, nullable=False)
    rating = db.Column(db.SmallInteger, nullable=True)
    assessment = db.Column(db.Text)
    last_modified = db.Column(db.TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow)

    # CheckConstraint für das Feld 'rating' (zwischen 1 und 10)
    __table_args__ = (
        db.CheckConstraint('rating BETWEEN 1 AND 10', name='rating_check'),
    )

    def to_dict(self):
        return {
            "id": self.id,
            "department": self.department,
            "statement": self.statement,
            "success_criteria": self.success_criteria,
            "rating": self.rating,
            "assessment": self.assessment,
            "last_modified": self.last_modified,
        }
