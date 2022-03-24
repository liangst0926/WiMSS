from flask import (
  Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.exceptions import abort

from app.auth import login_required
from app.db import get_db_or_fail
from . import utils

bp = Blueprint('summary', __name__)


@bp.route('/')
@login_required
def summary():
  db = get_db_or_fail()
  cursor = db.cursor()

  sqls = utils.get_sqls('summary.sql')

  cursor.execute(sqls[0])
  num_cities = cursor.fetchone()[0]

  cursor.execute(sqls[1])
  num_stores = cursor.fetchone()[0]

  cursor.execute(sqls[2])
  num_gs_stores = cursor.fetchone()[0]

  cursor.execute(sqls[3], (g.user[0],))
  num_viewable_stores = cursor.fetchone()[0]

  cursor.execute(sqls[4])
  num_manufacturers = cursor.fetchone()[0]

  cursor.execute(sqls[5])
  num_products = cursor.fetchone()[0]

  cursor.execute(sqls[6])
  num_special_savings_days = cursor.fetchone()[0]

  return render_template(
    'summary.html',
    num_cities=num_cities,
    num_stores=num_stores,
    num_gs_stores=num_gs_stores,
    num_viewable_stores=num_viewable_stores,
    num_manufacturers=num_manufacturers,
    num_products=num_products,
    num_special_savings_days=num_special_savings_days,
  )


@bp.route('/store_details')
def store_details():
  user_id = session.get('user_id')
  db = get_db_or_fail()
  cursor = db.cursor()
  sql = utils.get_sqls('store_details.sql')[0]
  cursor.execute(sql, (user_id, ))

  store_details = cursor.fetchall()

  return render_template('store_details.html', store_details=store_details)

@bp.route('/not_implemented')
@login_required
def not_implemented():
  """For a page which is not yet implemented."""
  return render_template('not_implemented.html')
