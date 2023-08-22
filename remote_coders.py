from flask import Flask, request, render_template, flash, redirect, url_for
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
from flask_bcrypt import Bcrypt, check_password_hash, generate_password_hash
import datetime
import os
from User import User, db
from Product import Product

app = Flask("watches_store")

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['UPLOAD_FOLDER'] = "./static/imgs/"
db.init_app(app)
# A secret key generated using secrets.token_hex()
app.config['SECRET_KEY'] = '7837d00905efa9242080679b5d6a58db405a2e367fc3f0ac93d7e177aec4addd'
# Wrap our app through Bcrypt to use Bcrypt to hash passwords
bcrypt = Bcrypt(app)
# Wrap our app through login_manager to be able to use login features
login_manager = LoginManager()
login_manager.init_app(app)

# Creat Our database
# Actually I don't know why this line for but to avoid error of calling out of app context
# https://flask.palletsprojects.com/en/2.2.x/appcontext/
# https://stackoverflow.com/questions/57734132/flask-application-context-app-app-context-push-works-but-cant-get-with-ap
app.app_context().push()
db.create_all()

# Login Stuff
# Login manager to allow us use of the logged in user methods by saving the user_id


@login_manager.user_loader
def load_user(id):
    return User.query.get(id)


login_manager.login_view = 'login'


# Instantiate our class wit a new user which will be accessd on rigester or login

# function to be used whenever call an HTML file but will use it only with index as other templates will be rendered with render_template method
def get_html(page):
    html_file = open("./templates/" + page + ".html")
    content = html_file.read()
    html_file.close()
    return content

# Get the home page


@app.route("/")
def index():
    return render_template("./index.html")

# Signup Page


@app.route("/signup", methods=['GET', 'POST'])
def signup():
    # Check if we request using GET then render the form template
    if request.method == 'GET':
        return render_template("./signup.html")
    # If request is POST then take the form data and add it to the database
    if request.method == 'POST':
        try:
            # This a check if the email is already exists
            email = request.form.get("email")
            user = User.query.filter_by(email=email).first()
            if user is None:
                # Get the data from the sign up form
                username = request.form.get("user_name")
                password = request.form.get("password")
                hashed_password = generate_password_hash(password)
                mobile = request.form.get("mobile")
                # Instantiate our User class
                new_user = User(
                    username=username, password=hashed_password, email=email, mobile=mobile)
                # Add to database and save it using commit
                db.session.add(new_user)
                db.session.commit()
                # Return the homepage flashing some messages
                flash("Signed up Successfully!")
                return redirect(url_for("login"))
            else:
                flash("Sorry This email already exists")
                return redirect(url_for("signup"))
        except:
            flash("Error in insert operation, please try again later")
            return redirect(url_for("signup"))

# Login Form


@app.route("/login", methods=["GET", "POST"])
def login():
    # Check if the request is GET then render the login page
    if request.method == "GET":
        return render_template("./login.html")
    # if request is POST then take the data and check if it's a valid data
    if request.method == "POST":
        try:
            #  Query the db using the provided email
            email = request.form.get("email")
            user = User.query.filter_by(email=email).first()
            # If user exists then check the given password
            if user:
                if check_password_hash(user.password, request.form.get("password")):
                    login_user(user)
                    flash("Logged In Successfully")
                    return redirect(url_for("index"))
                else:
                    flash("Wrong Password")
                    return redirect(url_for("login"))
            else:
                flash("Invalid credentials")
                return redirect(url_for("login"))
        except:
            flash("Server Error, please try again later")
            return redirect(url_for("login"))

# Log User Out


@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Logged Out Successfully")
    return redirect(url_for("index"))
# Update Profile


@app.route("/edit_profile", methods=["GET", "POST"])
@login_required
def edit():
    if request.method == "GET":
        return render_template("./edit_profile.html")
    if request.method == "POST":
        try:
            # Get the user input
            # Ternary Operator so if the user didn't add a new user name or new email use the old ones
            new_email = request.form.get("email") if request.form.get(
                "email") != "" else current_user.email
            new_username = request.form.get("username") if request.form.get(
                "username") != "" else current_user.username
            # Update the user name and email
            current_user.update_email(new_email)
            current_user.update_username(new_username)
            flash("Email Updated")
            return redirect(url_for("index"))
        except:
            flash("Invalid data")
            return redirect(url_for("edit"))
#######
# Product Handlers
#######
# Product Routing Page


@app.route("/product", methods=['GET'])
@login_required
def product():
    # Check if the user is admin (maybe this a bad practice for hardcoding the pass and email but just for test)
    if check_password_hash(current_user.password, "admin123") and current_user.email == "admin@gmail.com":
        return render_template("./product.html")
    else:
        flash("Only for admins")
        return redirect(url_for("index"))
# Add Product Hanlder


@app.route("/add_product", methods=['GET', 'POST'])
@login_required
def add_product():
    # Check if we request using GET then render the form template
    if request.method == 'GET':
        return render_template("./addproduct.html")
    # If request is POST then take the form data and add it to the database
    if request.method == 'POST':
        try:
            # This a check if the email is already exists
            model = request.form.get("model")
            product_name = request.form.get("product_name")
            product = Product.query.filter_by(
                model=model, product_name=product_name).first()
            if product is None:
                # Get the data from the sign up form
                color = request.form.get("color")
                price = request.form.get("price")
                image = request.files['image']
                # Save the image to the folder specified
                image.save(os.path.join(
                    app.config['UPLOAD_FOLDER'], image.filename))
                # Instantiate our User class
                new_product = Product(
                    product_name=product_name, model=model, color=color, price=price, image=image.filename)
                # Add to database and save it using commit
                db.session.add(new_product)
                db.session.commit()
                # Return the homepage flashing some messages
                flash("Product Added Successfully!")
                return redirect(url_for("index"))
            else:
                flash("Sorry this product exists")
                return redirect(url_for("product"))
        except:
            flash("Error in insert operation, please try again later")
            return redirect(url_for("product"))
# Delete Product Hanlder


@app.route("/delete_product", methods=['GET', 'POST'])
@login_required
def delete_product():
    # Check if we request using GET then render the form template
    if request.method == 'GET':
        return render_template("./deleteproduct.html")
    # If request is POST then take the form data and delete it from the database
    if request.method == 'POST':
        try:
            # Check if the product is  exists the delete it
            product_name = request.form.get("product_name")
            model = request.form.get("model")
            product = Product.query.filter_by(
                model=model, product_name=product_name).first()
            if product:
                # Get the data from the sign up form
                product.delete_product(product)
                # Return the homepage flashing some messages
                flash("Product Deleted Successfully!")
                return redirect(url_for("index"))
            else:
                flash("Sorry this product doesn't exist")
                return redirect(url_for("product"))
        except:
            flash("Error in insert operation, please try again later")
            return redirect(url_for("product"))
#############
# Shop Handler
# Get the shop page (available only for our User)


@app.route("/shop")
@login_required
def shop():
    # Get the products from the db and pass them to the html
    products = Product.query.all()
    return render_template("./shop.html", products=products)
# Cart Page Routing
# Get the cart page


@app.route("/cart")
def cart():
    return render_template("/cart.html")
# Placing User Orders


@app.route("/place_order")
def place_order():
    flash("Order Placed Successfully")
    return render_template("/index.html")

# Products Reviews Handler
# Reviews for diffrent products page


@app.route('/reviews', methods=['GET', 'POST'])
def review():
    # We used read and write from files so will use the old method to open the html not render
    if request.method == 'GET':
        # Open the file, read it's content and then close it
        try:
            # Open the text file to read from it then close it
            review_file = open("./reviews.txt")
            reviews = review_file.read().split("\n")
            # Get the available products for new reviews
            products = Product.query.all()
            review_file.close()
            return render_template("./reviews.html", reviews=reviews, products=products)
        except:
            flash("No reviews yet, add your review below")
            return render_template("./reviews.html")
    if request.method == 'POST':
        # Open the review file
        review_file = open("./reviews.txt", "a")
        # Get the user review data
        # user_name = request.form.get('user_name')
        product_name = request.form.get('product_name')
        review = request.form.get('review')
        time = str(datetime.datetime.now())
        new_review = [" Username: " + current_user.username, " Product_Name: " +
                      product_name, " Review: "+review, " Reviewd On: " + time]
        # Loop over given review and write it on separated lines
        for review in new_review:
            review_file.write(str(review))
        # Break each review with a significant mark
        review_file.write("\n")
        # review_file.write("###")
        review_file.close()
        flash("We Appreciate Your Feedback, Thank You")
        return render_template("./index.html",)
    return redirect(url_for("index"))
