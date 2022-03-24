from flask import (
  Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from app.auth import login_required
from app.db import get_db_or_fail
from . import utils

bp = Blueprint('store_revenue_by_year_by_state', __name__)


@bp.route('/store_revenue_by_year_by_state')
def report():
  db = get_db_or_fail()
  cursor = db.cursor()
  sql = utils.get_sqls('store_revenue_by_year_by_state.sql')[0]
  cursor.execute(sql)
  summary = cursor.fetchall()
  return render_template('select_state.html', summary=summary)


@bp.route('/store_revenue_by_year_by_state/<state>')
def state_report(state):
  db = get_db_or_fail()
  cursor = db.cursor()
  sql = utils.get_sqls('store_revenue_by_year_by_state.sql')[0]
  cursor.execute(sql)
  summary = cursor.fetchall()

  sql = utils.get_sqls('store_revenue_by_year_by_state.sql')[1]
  cursor.execute(sql, (state, ))
  details = cursor.fetchall()

  return render_template('store_revenue_by_year_by_state.html', state=state, summary=summary, details=details)



