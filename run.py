from app import create_app

app = create_app()

if __name__ == '__main__':
    # Set environment for production
    if app.config.get('DEBUG'):
        app.run(debug=True, host='0.0.0.0', port=5000)
    else:
        app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
