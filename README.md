# Heroku-Sample Easy to Deploy it.


## SETUP Environment

Python: 3.3
Postgres
Flask

    source venv/bin/activate
    pip install -r requirements.txt

set db_path like 'postgresql://username:password@hostname/db_name' at basic_app.config.py 

##Add Addon for Postgresql

heroku addons:add heroku-postgresql:dev


 
##Confirm status of db.
heroku config



##How to migrate your app at remote/production

    alembic revision --autogenerate -m "update"
    alembic upgrade head
    git push heroku master

    heroku run alembic upgrade head


##Run Python at remote

    heroku run python -i

##Run Shell Script at remote

    heroku run source hello.sh

##Connect to the production's database via psql

    $ heroku pg:psql



