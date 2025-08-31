from flask import Blueprint, jsonify
from app import db

health_bp = Blueprint('health', __name__)

@health_bp.route('/health')
def health_check():
    """Health check endpoint for Render"""
    try:
        # Test database connection
        db.session.execute('SELECT 1')
        db_status = 'healthy'
    except Exception as e:
        db_status = f'unhealthy: {str(e)}'
    
    return jsonify({
        'status': 'healthy',
        'database': db_status,
        'timestamp': '2024-08-31T21:45:00Z'
    })

@health_bp.route('/')
def root():
    """Root endpoint for health check"""
    return jsonify({
        'message': 'Roomsy App is running!',
        'status': 'healthy'
    })
