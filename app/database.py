"""
Database connection handler for Roomsy app
Supports multiple PostgreSQL drivers and fallback to SQLite
"""

import os
from sqlalchemy import create_engine, text
from sqlalchemy.exc import OperationalError, ImportError

def get_database_url():
    """
    Get database URL with fallback handling
    Returns a valid SQLAlchemy database URL
    """
    database_url = os.environ.get('DATABASE_URL')
    
    if not database_url:
        print("No DATABASE_URL found, using SQLite fallback")
        return 'sqlite:///roomsy.db'
    
    # Fix Render PostgreSQL URL format
    if database_url.startswith('postgres://'):
        database_url = database_url.replace('postgres://', 'postgresql://', 1)
        print(f"Converted postgres:// to postgresql://")
    
    # Test the connection
    try:
        engine = create_engine(database_url, echo=False)
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
            print("✅ Database connection successful")
            return database_url
    except Exception as e:
        print(f"❌ Database connection failed: {e}")
        print("Falling back to SQLite")
        return 'sqlite:///roomsy.db'

def create_database_engine():
    """
    Create database engine with proper error handling
    """
    database_url = get_database_url()
    
    try:
        if database_url.startswith('postgresql://'):
            # Try to use pg8000 first (Python 3.13 compatible)
            try:
                import pg8000
                print("✅ Using pg8000 PostgreSQL driver")
            except ImportError:
                print("⚠️ pg8000 not available, trying psycopg2")
                try:
                    import psycopg2
                    print("✅ Using psycopg2 PostgreSQL driver")
                except ImportError:
                    print("❌ No PostgreSQL drivers available, falling back to SQLite")
                    database_url = 'sqlite:///roomsy.db'
        
        engine = create_engine(database_url, echo=False)
        return engine
        
    except Exception as e:
        print(f"❌ Failed to create database engine: {e}")
        print("Falling back to SQLite")
        return create_engine('sqlite:///roomsy.db', echo=False)
