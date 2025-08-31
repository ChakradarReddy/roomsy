from flask import Blueprint, render_template, request
from app.models.apartment import Apartment
from app.models.user import User

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    apartments = Apartment.query.filter_by(is_available=True).paginate(
        page=page, per_page=9, error_out=False
    )
    return render_template('main/index.html', apartments=apartments)

@main_bp.route('/apartment/<int:apartment_id>')
def apartment_detail(apartment_id):
    apartment = Apartment.query.get_or_404(apartment_id)
    return render_template('main/apartment_detail.html', apartment=apartment)

@main_bp.route('/search')
def search():
    query = request.args.get('q', '')
    city = request.args.get('city', '')
    min_price = request.args.get('min_price', type=float)
    max_price = request.args.get('max_price', type=float)
    
    apartments = Apartment.query.filter_by(is_available=True)
    
    if query:
        apartments = apartments.filter(
            Apartment.title.contains(query) | 
            Apartment.description.contains(query) |
            Apartment.address.contains(query)
        )
    
    if city:
        apartments = apartments.filter(Apartment.city.ilike(f'%{city}%'))
    
    if min_price is not None:
        apartments = apartments.filter(Apartment.price_per_month >= min_price)
    
    if max_price is not None:
        apartments = apartments.filter(Apartment.price_per_month <= max_price)
    
    apartments = apartments.all()
    
    return render_template('main/search.html', apartments=apartments, 
                         query=query, city=city, min_price=min_price, max_price=max_price)
