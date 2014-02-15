from flask import Blueprint
bp = Blueprint("users", __name__, template_folder="templates")
from basic_app.users import views

