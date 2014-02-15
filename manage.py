from basic_app import create_app,manager,db
from flask.ext.script import Manager
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.migrate import Migrate, MigrateCommand















@manager.command
def run():
    app = create_app()
    app.run(debug=True)
    return "hello"


@manager.command
def create_db():
    app= create_app()
    db.create_all()



if __name__ == "__main__":
    manager.run()

