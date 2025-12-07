from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from repositories.repository_factory import RepositoryFactory

listing_bp = Blueprint('listing', __name__, url_prefix='/listing')

@listing_bp.route('/create', methods=['GET', 'POST'])
def create_listing():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    
    if session.get('role') != 'Producer':
        flash("Access Denied: Producers only.", "warning")
        return redirect(url_for('home'))

    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        price = request.form.get('price')
        listing_type = request.form.get('type')
        image_url = request.form.get('image_url')

        listing_repo = RepositoryFactory.get_repository("listing")
        listing_repo.add_listing(title, description, price, listing_type, image_url, session['user_id'])
        
        flash("Listing created successfully!", "success")
        return redirect(url_for('home'))

    return render_template('listing/add_listing.html')

@listing_bp.route('/<int:listing_id>')
def view_listing(listing_id):
    listing_repo = RepositoryFactory.get_repository("listing")
    listing = listing_repo.get_listing_by_id(listing_id)
    
    if listing is None:
        flash("Listing not found!", "danger")
        return redirect(url_for('home'))
        
    return render_template('listing/view_listing.html', listing=listing)