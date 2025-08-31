#!/usr/bin/env python3
"""
Simple startup script for Roomsy app
Bypasses complex database initialization for production
"""

import os
from app import create_app

def start_app():
    """Start the Flask app"""
    try:
        print("🚀 Starting Roomsy app...")
        app = create_app()
        print("✅ App created successfully!")
        return app
    except Exception as e:
        print(f"❌ Failed to create app: {e}")
        return None

if __name__ == '__main__':
    app = start_app()
    if app:
        print("🎉 App is ready to run!")
    else:
        print("💥 App creation failed!")
