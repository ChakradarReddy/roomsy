from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app
from flask_login import login_required, current_user
from app.models.apartment import Apartment
from app.models.booking import Booking
from app import db, mail
from flask_mail import Message
from datetime import datetime, timedelta
import math

booking_bp = Blueprint('booking', __name__, url_prefix='/booking')

def validate_booking_dates(start_date, end_date, apartment):
    """Validate booking dates"""
    today = datetime.now().date()
    
    if start_date < today:
        return False, "Start date cannot be in the past"
    
    if end_date <= start_date:
        return False, "End date must be after start date"
    
    # Check minimum contract duration
    duration_months = math.ceil((end_date - start_date).days / 30)
    if duration_months < apartment.min_contract_duration:
        return False, f"Minimum contract duration is {apartment.min_contract_duration} months"
    
    return True, "Dates are valid"

@booking_bp.route('/<int:apartment_id>', methods=['GET', 'POST'])
@login_required
def book_apartment(apartment_id):
    apartment = Apartment.query.get_or_404(apartment_id)
    
    if not apartment.is_available:
        flash('This apartment is not available for booking.', 'error')
        return redirect(url_for('main.apartment_detail', apartment_id=apartment_id))
    
    if request.method == 'POST':
        start_date_str = request.form.get('start_date')
        end_date_str = request.form.get('end_date')
        
        # Validation
        if not start_date_str:
            flash('Start date is required.', 'error')
            return render_template('booking/book.html', apartment=apartment)
        
        if not end_date_str:
            flash('End date is required.', 'error')
            return render_template('booking/book.html', apartment=apartment)
        
        try:
            start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
            end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
        except ValueError:
            flash('Invalid date format. Please use YYYY-MM-DD format.', 'error')
            return render_template('booking/book.html', apartment=apartment)
        
        # Validate dates
        is_valid, message = validate_booking_dates(start_date, end_date, apartment)
        if not is_valid:
            flash(message, 'error')
            return render_template('booking/book.html', apartment=apartment)
        
        # Calculate duration and total amount
        duration_months = math.ceil((end_date - start_date).days / 30)
        total_amount = apartment.price_per_month * duration_months
        deposit_amount = total_amount * 0.2  # 20% deposit
        
        # Create booking
        try:
            booking = Booking(
                start_date=start_date,
                end_date=end_date,
                total_amount=total_amount,
                deposit_amount=deposit_amount,
                user_id=current_user.id,
                apartment_id=apartment.id
            )
            
            db.session.add(booking)
            db.session.commit()
            
            # Send confirmation email
            send_booking_confirmation(booking)
            
            flash('Booking created successfully! Please complete the deposit payment.', 'success')
            return redirect(url_for('booking.payment', booking_id=booking.id))
            
        except Exception as e:
            db.session.rollback()
            flash('An error occurred while creating the booking. Please try again.', 'error')
            return render_template('booking/book.html', apartment=apartment)
    
    return render_template('booking/book.html', apartment=apartment)

@booking_bp.route('/payment/<int:booking_id>')
@login_required
def payment(booking_id):
    booking = Booking.query.get_or_404(booking_id)
    
    if booking.user_id != current_user.id:
        flash('Access denied.', 'error')
        return redirect(url_for('main.index'))
    
    return render_template('booking/payment.html', booking=booking)

@booking_bp.route('/confirm/<int:booking_id>')
@login_required
def confirm_booking(booking_id):
    booking = Booking.query.get_or_404(booking_id)
    
    if booking.user_id != current_user.id:
        flash('Access denied.', 'error')
        return redirect(url_for('main.index'))
    
    # In a real application, this would integrate with a payment gateway
    # For now, we'll simulate payment confirmation
    try:
        booking.deposit_paid = True
        booking.status = 'confirmed'
        db.session.commit()
        
        # Send confirmation email
        send_booking_confirmation(booking)
        
        flash('Payment confirmed! Your booking is now active.', 'success')
        return redirect(url_for('main.index'))
        
    except Exception as e:
        db.session.rollback()
        flash('An error occurred while confirming the payment. Please try again.', 'error')
        return redirect(url_for('booking.payment', booking_id=booking.id))

@booking_bp.route('/my-bookings')
@login_required
def my_bookings():
    bookings = Booking.query.filter_by(user_id=current_user.id).order_by(Booking.created_at.desc()).all()
    return render_template('booking/my_bookings.html', bookings=bookings)

def send_booking_confirmation(booking):
    """Send booking confirmation email"""
    try:
        msg = Message(
            subject=f'Booking Confirmation - {booking.apartment.title}',
            sender=current_app.config['MAIL_USERNAME'],
            recipients=[booking.user.email]
        )
        
        msg.body = f'''
        Dear {booking.user.username},
        
        Your booking has been confirmed!
        
        Apartment: {booking.apartment.title}
        Address: {booking.apartment.address}
        Start Date: {booking.start_date}
        End Date: {booking.end_date}
        Total Amount: ${booking.total_amount:.2f}
        Deposit Amount: ${booking.deposit_amount:.2f}
        
        Thank you for choosing Roomsy!
        
        Best regards,
        The Roomsy Team
        '''
        
        mail.send(msg)
    except Exception as e:
        # Log error but don't fail the booking
        current_app.logger.error(f'Failed to send email: {e}')
