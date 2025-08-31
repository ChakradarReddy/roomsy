# Roomsy - Apartment Rental Platform

A modern, production-ready web application for listing and booking apartments. Built with Python Flask, featuring user authentication, apartment management, booking system, and payment integration.

## Features

### For Customers
- **User Registration & Login**: Secure authentication system
- **Browse Apartments**: View apartment listings with photos, details, and pricing
- **Search & Filter**: Find apartments by location, price, and amenities
- **Booking System**: Reserve apartments with deposit payment
- **Booking Management**: Track bookings and payment status
- **Email Notifications**: Receive booking confirmations

### For Property Owners
- **Owner Dashboard**: Manage apartment listings and view bookings
- **Add Apartments**: Create detailed apartment listings
- **Edit Listings**: Update apartment information and availability
- **Payment Tracking**: Monitor deposit and full payments
- **Booking Management**: View and manage tenant bookings

## Technology Stack

- **Backend**: Python 3.9+, Flask 2.3.3
- **Database**: SQLite (development), PostgreSQL (production)
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **Authentication**: Flask-Login
- **Forms**: Flask-WTF with CSRF protection
- **Email**: Flask-Mail
- **Deployment**: Gunicorn, Render-ready

## Installation & Setup

### Prerequisites
- Python 3.9 or higher
- pip (Python package installer)

### Local Development

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd roomsy-app
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set environment variables**
   ```bash
   export FLASK_APP=run.py
   export FLASK_ENV=development
   export SECRET_KEY=your-secret-key-here
   ```

5. **Run the application**
   ```bash
   python run.py
   ```

6. **Access the application**
   - Open your browser and go to `http://localhost:5000`
   - Register as a new user or owner
   - Start exploring apartments!

### Production Deployment

The application is configured for deployment on Render:

1. **Environment Variables**
   - `SECRET_KEY`: Secure random string for session encryption
   - `DATABASE_URL`: PostgreSQL connection string
   - `MAIL_USERNAME`: Email username for notifications
   - `MAIL_PASSWORD`: Email password for notifications

2. **Database Setup**
   - The application automatically creates tables on first run
   - For production, use PostgreSQL for better performance

3. **Deploy to Render**
   - Connect your GitHub repository
   - Set build command: `pip install -r requirements.txt`
   - Set start command: `gunicorn run:app`
   - Configure environment variables

## Project Structure

```
roomsy-app/
├── app/
│   ├── __init__.py          # Flask app factory
│   ├── models/              # Database models
│   ├── routes/              # Route handlers
│   ├── templates/           # HTML templates
│   ├── static/              # CSS, JS, images
│   └── utils/               # Utility functions
├── requirements.txt          # Python dependencies
├── config.py                # Configuration settings
├── run.py                   # Application entry point
├── Procfile                 # Render deployment
└── README.md                # This file
```

## Database Models

### User
- Basic user information and authentication
- Owner flag for property management
- Relationship to apartments and bookings

### Apartment
- Property details (title, description, address)
- Amenities (bedrooms, bathrooms, area)
- Pricing and contract terms
- Availability status

### Booking
- Reservation details and dates
- Payment tracking (deposit and full payment)
- Booking status management

## API Endpoints

### Authentication
- `POST /login` - User login
- `POST /register` - User registration
- `GET /logout` - User logout

### Main Pages
- `GET /` - Home page with apartment listings
- `GET /apartment/<id>` - Apartment details
- `GET /search` - Search apartments

### Owner Management
- `GET /owner/dashboard` - Owner dashboard
- `POST /owner/apartment/new` - Create new apartment
- `POST /owner/apartment/<id>/edit` - Edit apartment
- `GET /owner/apartment/<id>/delete` - Delete apartment

### Booking System
- `POST /booking/<apartment_id>` - Create booking
- `GET /booking/payment/<booking_id>` - Payment page
- `GET /booking/confirm/<booking_id>` - Confirm payment
- `GET /booking/my-bookings` - User's bookings

## Payment Integration

The application includes a simulated payment system that redirects users to contact support for actual payment processing:

**Contact Information:**
- Email: chakradarreddy12@gmail.com
- Phone: +919866827205
- Contact Person: Chakradar Reddy

## Security Features

- CSRF protection on all forms
- Secure password hashing
- User authentication and authorization
- Input validation and sanitization
- SQL injection protection via SQLAlchemy

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License.

## Support

For technical support or questions about the application, please contact:
- Email: chakradarreddy12@gmail.com
- Phone: +919866827205

## Future Enhancements

- Image upload and management
- Advanced search filters
- Review and rating system
- Mobile app development
- Real-time chat support
- Advanced payment gateway integration
- Property inspection scheduling
- Maintenance request system
