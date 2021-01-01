# FRONT END

## Description about app

- This basic offers app consists of three views as follows:
  - Login view that handles user authentication.
  - Offer List view that lists offers via cards and Apply Filter button that applies the filter: _Transaction type as deposit offers and amount bigger than 50.000 TRY. **Offer List view has pagination support.**_
  - Offer detail view to display the offer details.

## Technologies/Libraries Used

- React Router Dom : To wrap all views into router in App.js.
- [Bootstrap](https://getbootstrap.com/): the world's most popular front-end open source toolkit.

## Available Scripts

In the project directory, you can run:

### `yarn install`

Install the node dependencies before run the app.

### `yarn start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

The page will reload if you make edits.\
You will also see any lint errors in the console.

### `yarn build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

#

# BACK END

## Before You Start

**In The backend folder:**

- Install the app requirements via [requirements.txt](backend/requirements.txt) folder via ```pip3 install -r requirements.txt```
- Init the db via ```python3 manage.py initdb``` command (You can use ```python3 manage.py dropdb``` to drop db)
- Create the app database via ```python3 create_db.py``` command.
- After above steps you are ready to start the app via ```python3 manage.py runserver``` command.


## Description about app

- This basic Flask e commerce app consists of views as follows:
  - Home view that handles the Flask/Python Basics Assignment(Authentication not needed).
  - Login view that handles user authentication.
  - Profile view to display detailed user information.
  - Products view to display the products via descriptions in table with _Buy Now_ and _Add to Cart_ features.
  - Cart view to display the products that added to the cart by user. _Buy Now_, _Remove From Cart_ and _Checkout_ features are available in this page.
- The app has user Login/Logout feature that implemented via Flask-Login.
- The app has _Buy Now_ as mentioned above in both Products and Cart views. After clicking _Buy Now_ button, Current Stock of the product is updated.
- Each user has own shopping cart and non-cleared shopping cart is saved for future log-ins.
- Product categories can be added via editing [create_db.py](backend/create_db.py) file
- The app has own database that the all users share that is created and managed via Flask-SQLAlchemy.
- Passwords in the app is saved to the db with hashes. _werkzeug.security_ is used to generate_password_hash method.
- The app has stock management feature (Currently users can not add/remove products).
- Bootstrap is used to styling the app.

