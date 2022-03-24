import functools

from flask import (
  Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from app.db import get_db_or_fail
bp = Blueprint('auth', __name__, url_prefix='/auth')



def get_user_type(db, user_name):
  cursor = db.cursor()
  cursor.execute('SELECT * FROM CorporateUser WHERE user_name = %s', (user_name, ))
  results = cursor.fetchone()
  if results is not None:
    return "corporate_user"

  cursor.execute('SELECT * FROM Manager WHERE user_name = %s', (user_name, ))
  results = cursor.fetchone()
  if results is not None:
    return "manager"

  cursor.execute('SELECT * FROM MarketingUser WHERE user_name = %s', (user_name, ))
  results = cursor.fetchone()
  if results is not None:
    return "marketing_user"

  return None


@bp.route('/login', methods=('GET', 'POST'))
def login():
  if request.method == 'POST':
    user_name = request.form['username']
    password = request.form['password']
    db = get_db_or_fail()
    error = None
    cursor = db.cursor()
    cursor.execute(
      'SELECT user_name, password FROM User WHERE user_name = %s', (user_name,)
    )
    user = cursor.fetchone()

    if user is None:
      error = 'Incorrect username.'
    elif not user[1] == password:
      error = 'Incorrect password.'

    if error is None:
      session.clear()
      session['user_id'] = user[0]
      session['user_type'] = get_user_type(db, user[0])
      return redirect(url_for('summary'))

    flash(error)

  return render_template('login.html')


@bp.before_app_request
def load_logged_in_user():
  user_id = session.get('user_id')

  if user_id is None:
    g.user = None
  else:
    db = get_db_or_fail()
    error = None
    cursor = db.cursor()
    cursor.execute(
      'SELECT * FROM user WHERE user_name = %s', (user_id,)
    )
    g.user = cursor.fetchone()


@bp.route('/logout')
def logout():
  session.clear()
  return redirect(url_for('summary'))


def login_required(view):
  @functools.wraps(view)
  def wrapped_view(**kwargs):
    if g.user is None:
      return redirect(url_for('auth.login'))

    return view(**kwargs)

  return wrapped_view


