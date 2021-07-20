####################################################
# # app.py
# ----
# 
# Written in the Python 3.7.9 Environment
# 
# By Nicole Lund 
# 
# This Python script stores scraped web data in a postgreSQL DB 
# and displays on a webpage.
####################################################

# Import Dependencies
from flask import Flask, render_template, redirect
import os
import refresh_data

# Setup Flask
app = Flask(__name__)

# # Setup Database
# from flask_sqlalchemy import SQLAlchemy
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '')
# # Remove tracking modifications
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)

# Create index.html route
@app.route("/")
def index():
    refreshed_data = refresh_data.refresh()
    print("Index: ")
    print(refreshed_data)

    # Delete existing collection

    # Insert refreshed data into db

    return render_template("index.html", refreshed_data=refreshed_data)


if __name__ == "__main__":
    app.run(debug=True)