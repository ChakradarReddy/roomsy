from app import create_app
import os

# Set FLASK_ENV to development if not already set
if os.environ.get('FLASK_ENV') is None:
    os.environ['FLASK_ENV'] = 'development'

app = create_app()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
