from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

app = Flask(__name__)
Bootstrap(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # Use SQLite as the database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable Flask-SQLAlchemy modification tracking
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    model = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    distance = db.Column(db.Integer, nullable=False)
    owner = db.Column(db.String(100), nullable=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/suggest_car', methods=['POST'])
def suggest_car():
    try:
        user_budget = int(request.form.get('budget'))
        available_cars = Car.query.filter(Car.distance < user_budget).all()

        for car in available_cars:
            print(f"Found car: {car.name}, {car.model}, {car.year}, {car.distance}, {car.owner}")

        return render_template('result.html', cars=available_cars)


    except Exception as e:
        print(f"Error in suggest_car route: {e}")
        return "An error occurred. Please check the server logs for details.", 500


@app.route('/express_interest', methods=['POST'])
def express_interest():
    user_name = request.form.get('userName')
    user_mobile = request.form.get('userMobile')

    # Example: Process the form data as needed (replace with your actual logic)
    # For demonstration purposes, just printing the data
    print(f"Expressing interest from {user_name} with mobile number {user_mobile}")

    return "Thank you for expressing interest! We'll get in touch with you soon."

if __name__ == '__main__':
    # Create the database tables before running the app
    db.create_all()
    app.run(debug=True)

