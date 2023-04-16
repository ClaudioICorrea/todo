from flask import(
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
from todo.auth import login_required
from todo.db import get_db

bp = Blueprint('todo',__name__)
@bp.route('/')
@login_required
def index():
    db, c = get_db()
    c.execute(
        'SELECT t.id, t.description, u.username, t.completed, t.created_at t FROM todo t JOIN user u on t.created_by = u.id ORDER BY created_at DESC'
    )
    todos = c.fetchall()
    return render_template('todo/index.html', todos=todos)