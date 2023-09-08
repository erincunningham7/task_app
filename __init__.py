import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# In order to use our hidden environment variables, need to import the 'env' package.
if os.path.exists("env.py"):
    import env  # noqa

# create an instance of the imported flask class
app = Flask(__name__)
# specify two app configuration variables
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")

# create an instance of the imported sqlalchemy class
db = SQLAlchemy(app)

from taskmanager import routes  # noqa