from flask_login import UserMixin
from app import db, bcrypt
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model, UserMixin):

    __tablename__ = 'user'

    username = db.Column(db.String)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    address = db.Column(db.String)
    id = db.Column(db.Integer, primary_key=True)
    _password = db.Column(db.String)
    user_cart = db.relationship('UserCart', backref='user', lazy=True, uselist=False)

    def __init__(self, username, first_name, last_name, address, _password):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self._password = generate_password_hash(_password)

    @property
    def password(self):
        return self._password

    def set_password(self, plaintext):
        self._password = generate_password_hash(plaintext)

    def check_password(self, plaintext):
        return check_password_hash(self.password, plaintext)


class Product(db.Model, UserMixin):

    __tablename__ = 'product'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    category = db.Column(db.String)
    stock = db.Column(db.String)
    brand = db.Column(db.String)
    rating = db.Column(db.String)
    dimensions = db.Column(db.String)
    reviews = db.Column(db.PickleType, nullable=True)

    def __init__(self, name, category, stock, brand, rating, dimensions, reviews):
        self.name = name
        self.category = category
        self.stock = stock
        self.brand = brand
        self.rating = rating
        self.dimensions = dimensions
        self.reviews = reviews

    def buy_now(self):
        self.stock = int(self.stock) - 1
        db.session.commit()


class UserCart(db.Model, UserMixin):
    __tablename__ = 'cart'

    id = db.Column(db.Integer, primary_key=True)
    product_ids = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self):
        pass

    def set_user_id(self, user_id):
        self.user_id = user_id

    def set_user_cart_items(self, product_ids):
        self.product_ids = product_ids

    def get_user_cart_items(self):
        return self.product_ids

    def add_to_cart(self, product_id):
        self.product_ids = str(product_id) if len(self.product_ids) == 0 \
            else self.product_ids+","+str(product_id)
        db.session.commit()

    def remove_from_cart(self, product_id):
        index = self.product_ids.index(str(product_id))
        if index == 1:
            self.product_ids = self.product_ids[2: len(self.product_ids)]
        elif index == len(self.product_ids)-1:
            self.product_ids = self.product_ids[0: len(self.product_ids)-2]
        else:
            self.product_ids = self.product_ids[0: index] + self.product_ids[index+1: len(self.product_ids)]
        db.session.commit()

    def empty_cart(self):
        self.product_ids = ""
        db.session.commit()
