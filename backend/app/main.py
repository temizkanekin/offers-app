import logging

from flask import render_template, request, Blueprint, redirect, url_for
from flask_login import login_required, current_user

from app.models import Product, UserCart

logger = logging.getLogger(__name__)

main = Blueprint('main', __name__)
#TODO yeni ürün ekleme, sipariş takibi

@main.route('/')
def base():
    return render_template('base.html')


@main.route('/home')
def home():
    return render_template('Home.html')


@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', current_user=current_user)


@main.route('/products')
@login_required
def products():
    products = Product.query.all()
    return render_template('products.html', products=products)


@main.route('/cart')
@login_required
def cart():
    cart_products = get_cart_products()
    return render_template('cart.html', products=cart_products)


@main.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    products = Product.query.all()
    cart = UserCart.query.filter_by(user_id=current_user.id).first()
    try:
        cart.add_to_cart(product_id)
        logger.info("%s added item to the cart with item id %s", current_user.username, product_id)
    except AttributeError:
        pass
    return render_template('products.html', products=products)


@main.route('/remove_from_cart/<int:product_id>')
def remove_from_cart(product_id):
    cart = UserCart.query.filter_by(user_id=current_user.id).first()
    cart_products = []
    try:
        cart.remove_from_cart(product_id)
        cart_products = get_cart_products()
        logger.info("%s removed item from the cart with item id %s", current_user.username, product_id)
    except AttributeError:
        pass
    return render_template('cart.html', products=cart_products)


@main.route('/checkout')
def checkout():
    cart_item_ids = UserCart.query.filter_by(user_id=current_user.id).first().get_user_cart_items().split(",")
    for product_id in cart_item_ids:
        product = Product.query.get(product_id)
        try:
            product.buy_now()
        except AttributeError:
            pass
    cart = UserCart.query.filter_by(user_id=current_user.id).first()
    cart.empty_cart()
    logger.info("Check out successful for user %s", current_user.username)
    return render_template('checkout.html')


def get_cart_products():
    user_cart = UserCart.query.filter_by(user_id=current_user.id).first()
    user_cart_items = user_cart.get_user_cart_items()
    if len(user_cart_items) > 0:
        cart_item_ids = user_cart_items.split(",")
        cart_products = []
        if cart_item_ids is not None:
            for product_id in cart_item_ids:
                cart_products.append(Product.query.get(product_id))
        logger.info("Get cart products completed for user %s", current_user.username)
        return cart_products
    else:
        return []


@main.route('/buy_now/<int:product_id>')
def buy_now(product_id):
    product = Product.query.get(product_id)
    try:
        product.buy_now()
        logger.info("%s bought product with id %s", current_user.username, product_id)
    except AttributeError:
        pass
    return redirect(url_for('main.products'))


@main.route('/input', methods=["GET", "POST"])
def input():
    input_a = request.form['inputA']
    input_b = request.form['inputB']
    if len(input_a) != 5 or not input_a.isalpha():
        message = "InputA value should contain only letters of length 5"
        return render_template('Home.html', message=message)
    return render_template('Home.html', message=handle_inputs(input_a, input_b))


def handle_inputs(input_a, input_b):
    res = ""
    for i in range(0, len(input_a)):
        res += input_a[i] * int(input_b[i])
    logger.info("Result is %s", res)
    return res
