Wacky Car Suggestion Site
Overview
Welcome to the Wacky Car Suggestion site, a fun and interactive web application that helps users find second-hand cars based on their budget. This project aims to provide an engaging user experience while showcasing the use of Flask, a lightweight and extensible web framework for Python.

Features
Budget-Based Car Suggestion: Users can input their budget, and the site suggests wacky cars available within that budget.
Car Details Page: Explore details about suggested cars, including name, model, year, distance traveled, and owner information.
Express Interest Form: Users can express their interest in a car by providing their name and mobile number.
Technologies Used
Python: The backend of the site is powered by Python, leveraging the Flask web framework.
HTML/CSS: The frontend is built using HTML for structure and CSS for styling.
Bootstrap: The site utilizes Bootstrap for responsive design and improved user interface components.
SQLite: Database management is handled by SQLite, a lightweight relational database.
Installation and Setup
Clone the repository to your local machine.

bash
git clone https://github.com/your-username/your-repo.git
Install dependencies using pip.

bash
pip install -r requirements.txt
Run the Flask development server.

bash
python app.py
Access the site at http://localhost:5000 in your web browser.

Database Management
The site uses Flask-SQLAlchemy for database interactions.
Flask-Migrate is employed for managing database migrations.
Database Commands
flask db init: Initialize the Flask-Migrate directory.
flask db migrate -m "Your migration message": Generate a migration.
flask db upgrade: Apply the migrations to create or update the database tables.
Contributing
Contributions are welcome! Feel free to open issues, suggest improvements, or submit pull requests.
