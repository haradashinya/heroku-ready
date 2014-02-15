from basic_app.users import bp
from basic_app.users.models import User
from basic_app import db


@bp.route("/")
def index():
    return "hello"


@bp.route("/create/<name>")
def create(name):
    u = User(name)
    db.session.add(u)
    db.session.commit()
    return 'created'


@bp.route("/all")
def all():
    return str(len(db.session.query(User).all()))




