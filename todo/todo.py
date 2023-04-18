
from datetime import datetime
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
        'SELECT t.id, t.created_at, t.description, u.username, t.completed  t FROM todo t JOIN user u on t.created_by = u.id ORDER BY created_at desc'
    )
    luke = c.fetchall()
    return render_template('todo/index.html', todos=luke)
@bp.route('/_create',methods=['GET','POST'])
@login_required
def _create():
    if request.method == 'POST':
        description = request.form['description']
        error = None
        if not description:
            error = 'Descripción es requerida'
        if error is not None:
            flash(error)
        else:
            db, c = get_db()
            c.execute(
                'insert into todo (description, completed, created_by)'
                ' values (%s,%s,%s)',
                (description, False, g.user['id'])
            )
            db.commit()
            return redirect(url_for('todo.index'))

    return render_template('todo/_create.html')

@bp.route('/<int:id>/_update', methods=['GET','POST'])
@login_required
def _update(id):
    return render_template('todo/_update.html', todo=todo)


@bp.route('/<int:id>/delete', methods=['POST'])
@login_required
def delete():
    return ''