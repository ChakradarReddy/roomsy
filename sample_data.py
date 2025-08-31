#!/usr/bin/env python3
"""
Sample data script for Roomsy application
Run this script to populate the database with sample apartments and users
"""

from app import create_app, db
from app.models.user import User
from app.models.apartment import Apartment
from werkzeug.security import generate_password_hash

def create_sample_data():
    app = create_app()
    
    with app.app_context():
        # Clear existing data
        db.drop_all()
        db.create_all()
        
        print("Creating sample users...")
        
        # Create sample users
        owner1 = User(
            username='john_owner',
            email='john@example.com',
            is_owner=True
        )
        owner1.password_hash = generate_password_hash('password123')
        
        owner2 = User(
            username='sarah_owner',
            email='sarah@example.com',
            is_owner=True
        )
        owner2.password_hash = generate_password_hash('password123')
        
        customer1 = User(
            username='mike_tenant',
            email='mike@example.com',
            is_owner=False
        )
        customer1.password_hash = generate_password_hash('password123')
        
        customer2 = User(
            username='lisa_tenant',
            email='lisa@example.com',
            is_owner=False
        )
        customer2.password_hash = generate_password_hash('password123')
        
        db.session.add_all([owner1, owner2, customer1, customer2])
        db.session.commit()
        
        print("Creating sample apartments...")
        
        # Create sample apartments
        apartment1 = Apartment(
            title='Modern Downtown Loft',
            description='Beautiful 2-bedroom loft in the heart of downtown. Features high ceilings, large windows, and modern appliances. Walking distance to restaurants, shopping, and public transportation.',
            address='123 Main Street',
            city='New York',
            state='NY',
            zip_code='10001',
            price_per_month=2500.00,
            min_contract_duration=12,
            bedrooms=2,
            bathrooms=2,
            area_sqft=1200,
            owner_id=owner1.id
        )
        
        apartment2 = Apartment(
            title='Cozy Garden Apartment',
            description='Charming 1-bedroom apartment with a private garden. Perfect for nature lovers. Includes parking space and access to community amenities.',
            address='456 Oak Avenue',
            city='Los Angeles',
            state='CA',
            zip_code='90210',
            price_per_month=1800.00,
            min_contract_duration=6,
            bedrooms=1,
            bathrooms=1,
            area_sqft=800,
            owner_id=owner1.id
        )
        
        apartment3 = Apartment(
            title='Luxury High-Rise Condo',
            description='Premium 3-bedroom condo with stunning city views. Features include gym access, swimming pool, concierge service, and secure parking.',
            address='789 Luxury Boulevard',
            city='Miami',
            state='FL',
            zip_code='33101',
            price_per_month=3500.00,
            min_contract_duration=12,
            bedrooms=3,
            bathrooms=2,
            area_sqft=1800,
            owner_id=owner2.id
        )
        
        apartment4 = Apartment(
            title='Student-Friendly Studio',
            description='Affordable studio apartment perfect for students. Close to university campus, grocery stores, and public transportation. Utilities included.',
            address='321 College Drive',
            city='Boston',
            state='MA',
            zip_code='02101',
            price_per_month=1200.00,
            min_contract_duration=9,
            bedrooms=0,
            bathrooms=1,
            area_sqft=500,
            owner_id=owner2.id
        )
        
        apartment5 = Apartment(
            title='Family Home with Yard',
            description='Spacious 4-bedroom family home with large backyard. Great for families with children. Features include garage, laundry room, and storage space.',
            address='654 Family Circle',
            city='Austin',
            state='TX',
            zip_code='73301',
            price_per_month=2800.00,
            min_contract_duration=12,
            bedrooms=4,
            bathrooms=3,
            area_sqft=2200,
            owner_id=owner1.id
        )
        
        db.session.add_all([apartment1, apartment2, apartment3, apartment4, apartment5])
        db.session.commit()
        
        print("Sample data created successfully!")
        print("\nSample Users:")
        print("Owners:")
        print(f"  - {owner1.username} (password: password123)")
        print(f"  - {owner2.username} (password: password123)")
        print("Customers:")
        print(f"  - {customer1.username} (password: password123)")
        print(f"  - {customer2.username} (password: password123)")
        print("\nSample Apartments:")
        print(f"  - {apartment1.title} - ${apartment1.price_per_month}/month")
        print(f"  - {apartment2.title} - ${apartment2.price_per_month}/month")
        print(f"  - {apartment3.title} - ${apartment3.price_per_month}/month")
        print(f"  - {apartment4.title} - ${apartment4.price_per_month}/month")
        print(f"  - {apartment5.title} - ${apartment5.price_per_month}/month")

if __name__ == '__main__':
    create_sample_data()
