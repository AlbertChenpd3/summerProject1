import sqlite3
from datetime import datetime

import click
from flask import current_app, g
#current app is the flask application handling the request and g is an object used for each request

#creates and returns a db
def get_db():
    if 'db' not in g: #g; sepcial object created for each request
        g.db = sqlite3.connect(  current_app.config['DATABASE'],detect_types=sqlite3.PARSE_DECLTYPES) #connects us to a sqlite database file, pointed at by 'DATABASE'
        g.db.row_factory = sqlite3.Row #rows bheave like dicts so we can call them by name

    return g.db



#closes a db has to be registered with the application
def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

#have to edit
#right now executes schema.sql instructions using the database created in db
def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f: #uses schema.sql to open a file relative to the flaskr package, in this case in the same folder
        db.executescript(f.read().decode('utf8'))

@click.command('init-db')
def init_db_command(): #defines a command line command called init-db that calls the init_db function and shows a success message to the user.
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')
    sqlite3.register_converter("timestamp", lambda v: datetime.fromisoformat(v.decode()))# tells Python how to interpret timestamp values in the db converting the value to a datetime.datetime.

def init_app(app): #note: have to call the init-db command in command line ex): flask --app flaskr init-db
    app.teardown_appcontext(close_db) #tells flask to call close_db when cleaning up after the response
    app.cli.add_command(init_db_command) # adds a new command that can be called with the flask command