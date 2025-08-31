#!/usr/bin/env python3
"""
Simple test script to verify the Roomsy application works correctly
"""

import sys
import os

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_imports():
    """Test if all required modules can be imported"""
    try:
        from app import create_app, db
        from app.models.user import User
        from app.models.apartment import Apartment
        from app.models.booking import Booking
        print("✓ All imports successful")
        return True
    except ImportError as e:
        print(f"✗ Import error: {e}")
        return False

def test_app_creation():
    """Test if the Flask app can be created"""
    try:
        from app import create_app
        app = create_app()
        print("✓ Flask app created successfully")
        return True
    except Exception as e:
        print(f"✗ App creation error: {e}")
        return False

def test_database_connection():
    """Test if database connection works"""
    try:
        from app import create_app, db
        app = create_app()
        with app.app_context():
            db.create_all()
            print("✓ Database connection successful")
            return True
    except Exception as e:
        print(f"✗ Database error: {e}")
        return False

def main():
    """Run all tests"""
    print("Testing Roomsy application...")
    print("=" * 40)
    
    tests = [
        ("Import Test", test_imports),
        ("App Creation Test", test_app_creation),
        ("Database Test", test_database_connection)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\nRunning {test_name}...")
        if test_func():
            passed += 1
        else:
            print(f"✗ {test_name} failed")
    
    print("\n" + "=" * 40)
    print(f"Tests passed: {passed}/{total}")
    
    if passed == total:
        print("🎉 All tests passed! The application is ready to run.")
        print("\nTo start the application:")
        print("1. Install dependencies: pip install -r requirements.txt")
        print("2. Run the app: python run.py")
        print("3. Open browser: http://localhost:5000")
    else:
        print("❌ Some tests failed. Please check the errors above.")
        sys.exit(1)

if __name__ == '__main__':
    main()
