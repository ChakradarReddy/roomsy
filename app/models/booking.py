from app import db
from datetime import datetime

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    total_amount = db.Column(db.Float, nullable=False)
    deposit_amount = db.Column(db.Float, nullable=False)
    deposit_paid = db.Column(db.Boolean, default=False)
    full_payment_paid = db.Column(db.Boolean, default=False)
    status = db.Column(db.String(20), default='pending')  # pending, confirmed, cancelled, completed
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Foreign Keys
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    apartment_id = db.Column(db.Integer, db.ForeignKey('apartment.id'), nullable=False)
    
    def __repr__(self):
        return f'<Booking {self.id}>'
    
    @property
    def duration_months(self):
        """Calculate duration in months"""
        delta = self.end_date - self.start_date
        return (delta.days // 30) + 1
    
    @property
    def remaining_amount(self):
        """Calculate remaining amount after deposit"""
        return self.total_amount - self.deposit_amount
