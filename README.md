# Heroku-Sample Easy to Deploy it.


## SETUP Environment

Python: 3.3
Postgres
Flask


##Add Addon for Postgresql

heroku addons:add heroku-postgresql:dev

##Install alembic

heroku run pip install alembic
 
# データベースの設定を確認
heroku config


# How to migrate your app at production

git push heroku master
heroku run alembic upgrade head


Run Python at remote

    heroku run python -i

Run Shell Script at remote

    heroku run source hello.sh

Connect to the production's database via psql

    $ heroku pg:psql


