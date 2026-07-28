#this file handles all the work of creating rooms and registering rooms to computers

import functools

from flask import ( Blueprint, flash, g, redirect, render_template, request, session, url_for)
from werkzeug.security import check_password_hash, generate_password_hash

from main.db import get_db

bp = Blueprint('register', __name__, url_prefix='/register')


@bp.route('/registerRoom<roomName>',methods=('GET','POST'))
def registerRoom():
    db = get_db()
    if request.method == 'POST':
        roomName = request.form['roomName']
        #if not unique have an error
        roomHash = generate_password_hash
        db.execute('INSERT INTO roomList (roomName,roomHash) VALUES (?,?)' (roomName,roomHash))
        db.execute('INSERT INTO individualRooms (currentRoomHash) VALUES (?)',roomHash)  #placeholder)
        db.commit()
    return #have to return a template here

@bp.route('/registerComputerToRoom<computer#>',methods=('POST'))
def registerComputerToRoom():
    db = get_db()


    return