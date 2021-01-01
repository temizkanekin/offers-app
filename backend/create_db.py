from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# from tabledef import *
from app.models import User, Product, UserCart

engine = create_engine('sqlite:////tmp/test.db', echo=True)

# create a Session
Session = sessionmaker(bind=engine)
session = Session()

# Create objects
user = User("james", "james", "James", "James's Address", "123")
session.add(user)

user = User("lara", "lara", "Lara", "Lara's Address", "123")
session.add(user)

user = User("eric", "eric", "Eric", "Eric's Address", "123")
session.add(user)

product = Product("Macbook", "Electronics", 5, "Apple", "4", "100x100", ["nice", "good", "not enough"])
session.add(product)

product = Product("Vivobook", "Electronics", 100, "Asus", "3.5", "120x120", ["good for gaming"])
session.add(product)

product = Product("Thinkpad", "Electronics", 1500, "Lenovo", "3", "50x50", ["nice ultrabook"])
session.add(product)

product = Product("Latitude", "Electronics", 140, "Dell", "3.5", "50x50", ["good daily usage"])
session.add(product)

cart = UserCart()
cart.set_user_cart_items("1,2")
cart.set_user_id(3)
session.add(cart)

cart = UserCart()
cart.set_user_cart_items("")
cart.set_user_id(1)
session.add(cart)

cart = UserCart()
cart.set_user_cart_items("")
cart.set_user_id(2)
session.add(cart)
# commit the record the database
session.commit()

for student in session.query(User).filter(User.username == 'eric'):
    print(student.first_name, student.last_name, student.id)

for product in session.query(Product).filter(Product.brand == 'Apple'):
    print(product.stock, product.brand, product.id)

print(session.query(UserCart).first().product_ids)
