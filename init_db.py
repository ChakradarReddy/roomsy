#!/usr/bin/env python3
"""
Database initialization script for Roomsy app
Handles database setup with error handling
"""

import os
import sys
from app import create_app, db

def init_database():
    """Initialize database with error handling"""
    try:
        app = create_app()
        
        with app.app_context():
            print("Creating database tables...")
            db.create_all()
            print("✅ Database tables created successfully!")
            
            # Try to create sample data
            try:
                from sample_data import create_sample_data
                print("Creating sample data...")
                create_sample_data()
                print("✅ Sample data created successfully!")
            except Exception as e:
                print(f"⚠️  Sample data creation failed: {e}")
                print("Continuing without sample data...")
                
    except Exception as e:
        print(f"❌ Database initialization failed: {e}")
        print("This might be due to missing environment variables or database connection issues.")
        print("The app will continue with SQLite fallback.")
        return False
    
    return True

if __name__ == '__main__':
    success = init_database()
    if success:
        print("\n🎉 Database initialization completed successfully!")
    else:
        print("\n⚠️  Database initialization had issues, but app may still work.")
