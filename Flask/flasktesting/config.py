from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Create Flask app
app = Flask(__name__)

# Point SQLAlchemy to a persisted DuckDB file
app.config["SQLALCHEMY_DATABASE_URI"] = "duckdb:///mydb.duckdb"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize the db instance
db = SQLAlchemy(app)
