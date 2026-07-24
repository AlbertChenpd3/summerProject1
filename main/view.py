from flask import ( Blueprint, flash, g, redirect, render_template, request, session, url_for)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

bp = Blueprint('view', __name__, url_prefix='/view')
#should let the user view status based on the room using the hash

@bp.route('/view/<roomHash>',__name__,methods=['GET'])
def view(roomHash):
    db = get_db()
    status = db.execute()

    return roomHash #should return the html template
