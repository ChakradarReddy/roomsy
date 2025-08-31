from app import db
from datetime import datetime

class Apartment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    address = db.Column(db.String(500), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    state = db.Column(db.String(100), nullable=False)
    zip_code = db.Column(db.String(20), nullable=False)
    price_per_month = db.Column(db.Float, nullable=False)
    min_contract_duration = db.Column(db.Integer, nullable=False)  # in months
    bedrooms = db.Column(db.Integer, nullable=False)
    bathrooms = db.Column(db.Integer, nullable=False)
    area_sqft = db.Column(db.Integer, nullable=False)
    is_available = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Foreign Keys
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    # Relationships
    images = db.relationship('ApartmentImage', backref='apartment', lazy=True, cascade='all, delete-orphan')
    bookings = db.relationship('Booking', backref='apartment', lazy=True)
    
    def __repr__(self):
        return f'<Apartment {self.title}>'

class ApartmentImage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(255), nullable=False)
    caption = db.Column(db.String(200))
    is_primary = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Foreign Keys
    apartment_id = db.Column(db.Integer, db.ForeignKey('apartment.id'), nullable=False)
    
    def __repr__(self):
        return f'<ApartmentImage {self.filename}>'
