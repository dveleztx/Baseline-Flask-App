# Baseline-Flask-App
*This baseline is a template flask app that can be used to get going quickly without having to reinvent the wheel. Comes with account pages with session/cookie management.*

## Getting Started
*Things you will need to get working*

### Requirements

- PostgreSQL
  - Create Database
    - Have the [psycopg2](https://pypi.org/project/psycopg2/) library installed
    - Make sure to update the [db_session](https://github.com/dveleztx/Baseline-Flask-App/blob/master/example_com/data/db_session.py) file to connect to database.
  - Grant Permission to Postgres (or whatever user you end up using)
- Requirements.txt has the rest of the libraries you need

### ORM

This project is using SQLAlchemy for database transactions, you can change this to something else. However, with SQLAlchemy you can easily change to another database such as MySQL or SQLite3.
