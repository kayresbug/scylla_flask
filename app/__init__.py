from flask import Flask

app = Flask(__name__)

from app.admin.index import admin as admin

app.register_blueprint(admin)