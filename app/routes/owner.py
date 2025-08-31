from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app.models.apartment import Apartment, ApartmentImage
from app.models.booking import Booking
from app import db
import os
from werkzeug.utils import secure_filename

owner_bp = Blueprint('owner', __name__, url_prefix='/owner')

@owner_bp.route('/dashboard')
@login_required
def dashboard():
    if not current_user.is_owner:
        flash('Access denied. Owner privileges required.', 'error')
        return redirect(url_for('main.index'))
    
    apartments = Apartment.query.filter_by(owner_id=current_user.id).all()
    bookings = Booking.query.join(Apartment).filter(Apartment.owner_id == current_user.id).all()
    
    return render_template('owner/dashboard.html', apartments=apartments, bookings=bookings)

@owner_bp.route('/apartment/new', methods=['GET', 'POST'])
@login_required
def new_apartment():
    if not current_user.is_owner:
        flash('Access denied. Owner privileges required.', 'error')
        return redirect(url_for('main.index'))
    
    if request.method == 'POST':
        # Get form data
        title = request.form.get('title', '').strip()
        description = request.form.get('description', '').strip()
        address = request.form.get('address', '').strip()
        city = request.form.get('city', '').strip()
        state = request.form.get('state', '').strip()
        zip_code = request.form.get('zip_code', '').strip()
        price_per_month = request.form.get('price_per_month')
        min_contract_duration = request.form.get('min_contract_duration')
        bedrooms = request.form.get('bedrooms')
        bathrooms = request.form.get('bathrooms')
        area_sqft = request.form.get('area_sqft')
        
        # Validation
        errors = []
        
        # Required field validation
        if not title or len(title) < 5:
            errors.append('Title is required and must be at least 5 characters')
        
        if not description or len(description) < 20:
            errors.append('Description is required and must be at least 20 characters')
        
        if not address or len(address) < 5:
            errors.append('Address is required and must be at least 5 characters')
        
        if not city or len(city) < 2:
            errors.append('City is required and must be at least 2 characters')
        
        if not state or len(state) < 2:
            errors.append('State is required and must be at least 2 characters')
        
        if not zip_code:
            errors.append('ZIP code is required')
        
        # Numeric validation
        try:
            price_per_month = float(price_per_month)
            if price_per_month < 100 or price_per_month > 10000:
                errors.append('Price must be between $100 and $10,000')
        except (ValueError, TypeError):
            errors.append('Invalid price amount')
        
        try:
            min_contract_duration = int(min_contract_duration)
            if min_contract_duration < 1 or min_contract_duration > 60:
                errors.append('Contract duration must be between 1 and 60 months')
        except (ValueError, TypeError):
            errors.append('Invalid contract duration')
        
        try:
            bedrooms = int(bedrooms)
            if bedrooms < 0 or bedrooms > 10:
                errors.append('Number of bedrooms must be between 0 and 10')
        except (ValueError, TypeError):
            errors.append('Invalid number of bedrooms')
        
        try:
            bathrooms = float(bathrooms)
            if bathrooms < 0.5 or bathrooms > 10:
                errors.append('Number of bathrooms must be between 0.5 and 10')
        except (ValueError, TypeError):
            errors.append('Invalid number of bathrooms')
        
        try:
            area_sqft = int(area_sqft)
            if area_sqft < 100 or area_sqft > 10000:
                errors.append('Area must be between 100 and 10,000 square feet')
        except (ValueError, TypeError):
            errors.append('Invalid area')
        
        # If there are validation errors, show them and return
        if errors:
            for error in errors:
                flash(error, 'error')
            return render_template('owner/new_apartment.html', 
                                title=title, description=description, address=address,
                                city=city, state=state, zip_code=zip_code,
                                price_per_month=price_per_month, min_contract_duration=min_contract_duration,
                                bedrooms=bedrooms, bathrooms=bathrooms, area_sqft=area_sqft)
        
        # Create apartment if all validation passes
        try:
            apartment = Apartment(
                title=title,
                description=description,
                address=address,
                city=city,
                state=state,
                zip_code=zip_code,
                price_per_month=price_per_month,
                min_contract_duration=min_contract_duration,
                bedrooms=bedrooms,
                bathrooms=bathrooms,
                area_sqft=area_sqft,
                owner_id=current_user.id
            )
            
            db.session.add(apartment)
            db.session.commit()
            
            flash('Apartment listed successfully!', 'success')
            return redirect(url_for('owner.dashboard'))
            
        except Exception as e:
            db.session.rollback()
            flash('An error occurred while creating the apartment. Please try again.', 'error')
            return render_template('owner/new_apartment.html', 
                                title=title, description=description, address=address,
                                city=city, state=state, zip_code=zip_code,
                                price_per_month=price_per_month, min_contract_duration=min_contract_duration,
                                bedrooms=bedrooms, bathrooms=bathrooms, area_sqft=area_sqft)
    
    return render_template('owner/new_apartment.html')

@owner_bp.route('/apartment/<int:apartment_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_apartment(apartment_id):
    if not current_user.is_owner:
        flash('Access denied. Owner privileges required.', 'error')
        return redirect(url_for('main.index'))
    
    apartment = Apartment.query.get_or_404(apartment_id)
    
    if apartment.owner_id != current_user.id:
        flash('Access denied. You can only edit your own apartments.', 'error')
        return redirect(url_for('owner.dashboard'))
    
    if request.method == 'POST':
        # Similar validation as new_apartment
        title = request.form.get('title', '').strip()
        description = request.form.get('description', '').strip()
        address = request.form.get('address', '').strip()
        city = request.form.get('city', '').strip()
        state = request.form.get('state', '').strip()
        zip_code = request.form.get('zip_code', '').strip()
        price_per_month = request.form.get('price_per_month')
        min_contract_duration = request.form.get('min_contract_duration')
        bedrooms = request.form.get('bedrooms')
        bathrooms = request.form.get('bathrooms')
        area_sqft = request.form.get('area_sqft')
        
        # Validation (same as above)
        errors = []
        
        if not title or len(title) < 5:
            errors.append('Title is required and must be at least 5 characters')
        
        if not description or len(description) < 20:
            errors.append('Description is required and must be at least 20 characters')
        
        if not address or len(address) < 5:
            errors.append('Address is required and must be at least 5 characters')
        
        if not city or len(city) < 2:
            errors.append('City is required and must be at least 2 characters')
        
        if not state or len(state) < 2:
            errors.append('State is required and must be at least 2 characters')
        
        if not zip_code:
            errors.append('ZIP code is required')
        
        try:
            price_per_month = float(price_per_month)
            if price_per_month < 100 or price_per_month > 10000:
                errors.append('Price must be between $100 and $10,000')
        except (ValueError, TypeError):
            errors.append('Invalid price amount')
        
        try:
            min_contract_duration = int(min_contract_duration)
            if min_contract_duration < 1 or min_contract_duration > 60:
                errors.append('Contract duration must be between 1 and 60 months')
        except (ValueError, TypeError):
            errors.append('Invalid contract duration')
        
        try:
            bedrooms = int(bedrooms)
            if bedrooms < 0 or bedrooms > 10:
                errors.append('Number of bedrooms must be between 0 and 10')
        except (ValueError, TypeError):
            errors.append('Invalid number of bedrooms')
        
        try:
            bathrooms = float(bathrooms)
            if bathrooms < 0.5 or bathrooms > 10:
                errors.append('Number of bathrooms must be between 0.5 and 10')
        except (ValueError, TypeError):
            errors.append('Invalid number of bathrooms')
        
        try:
            area_sqft = int(area_sqft)
            if area_sqft < 100 or area_sqft > 10000:
                errors.append('Area must be between 100 and 10,000 square feet')
        except (ValueError, TypeError):
            errors.append('Invalid area')
        
        if errors:
            for error in errors:
                flash(error, 'error')
            return render_template('owner/edit_apartment.html', apartment=apartment)
        
        # Update apartment if validation passes
        try:
            apartment.title = title
            apartment.description = description
            apartment.address = address
            apartment.city = city
            apartment.state = state
            apartment.zip_code = zip_code
            apartment.price_per_month = price_per_month
            apartment.min_contract_duration = min_contract_duration
            apartment.bedrooms = bedrooms
            apartment.bathrooms = bathrooms
            apartment.area_sqft = area_sqft
            apartment.is_available = request.form.get('is_available') == 'on'
            
            db.session.commit()
            flash('Apartment updated successfully!', 'success')
            return redirect(url_for('owner.dashboard'))
            
        except Exception as e:
            db.session.rollback()
            flash('An error occurred while updating the apartment. Please try again.', 'error')
            return render_template('owner/edit_apartment.html', apartment=apartment)
    
    return render_template('owner/edit_apartment.html', apartment=apartment)

@owner_bp.route('/apartment/<int:apartment_id>/delete')
@login_required
def delete_apartment(apartment_id):
    if not current_user.is_owner:
        flash('Access denied. Owner privileges required.', 'error')
        return redirect(url_for('main.index'))
    
    apartment = Apartment.query.get_or_404(apartment_id)
    
    if apartment.owner_id != current_user.id:
        flash('Access denied. You can only delete your own apartments.', 'error')
        return redirect(url_for('owner.dashboard'))
    
    try:
        db.session.delete(apartment)
        db.session.commit()
        flash('Apartment deleted successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash('An error occurred while deleting the apartment. Please try again.', 'error')
    
    return redirect(url_for('owner.dashboard'))
