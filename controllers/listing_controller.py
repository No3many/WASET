from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from repositories import listing_repository
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




@listing_bp.route("/listing/<int:listing_id>/bid", methods=["POST"])
def place_bid(listing_id):
    if "user_id" not in session:
        flash("You must be logged in to bid.", "danger")
        return redirect(url_for("listing.view_listing", listing_id=listing_id))

    bidder_id = session["user_id"]
    bid_amount = float(request.form["bid_amount"])

    bid_repo = RepositoryFactory.get_bid_repository()
    highest_bid = bid_repo.get_highest_bid(listing_id) or 0

    if bid_amount <= highest_bid:
        flash("Bid must be higher than current highest bid.", "danger")
        return redirect(url_for("listing.view_listing", listing_id=listing_id))

    bid_repo.place_bid(listing_id, bidder_id, bid_amount)

    flash("Bid placed successfully!", "success")
    return redirect(url_for("listing.view_listing", listing_id=listing_id))

