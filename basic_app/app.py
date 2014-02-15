from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager
from flask.ext.migrate import Migrate,MigrateCommand
app = Flask(__name__)
import os
import basic_app.config as config
is_mac =  "Darwin" in os.uname()
if is_mac:
    print('mac')
    # local

    app.config['SQLALCHEMY_DATABASE_URI'] = config.db_path
else:
    print('linux')
    # remote
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')



db = SQLAlchemy(app)
migrate = Migrate(app,db)
manager = Manager(app)
manager.add_command("db",MigrateCommand)




@app.route('/')
def home():
    db.session.commit()
    return "hello"

@app.route("/create/<name>")
def create(name):
    try:
        u = User(name)
        db.session.add(u)
        db.session.commit()
    except:
        return 'err'
    return 'a'



if __name__ == '__main__':
    app.run(debug=True)

