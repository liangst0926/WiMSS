from flask import (
  Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from app.auth import login_required
from app.db import get_db_or_fail
from . import utils

bp = Blueprint('state_with_highest_volume_for_each_category', __name__)


@bp.route('/state_with_highest_volume_for_each_category')
def report():
  db = get_db_or_fail()
  cursor = db.cursor()
  sql = utils.get_sqls('state_with_highest_volume_for_each_category.sql')[0]
  cursor.execute(sql)

  summary = cursor.fetchall()

  return render_template('select_month_year.html', summary=summary)


@bp.route('/state_with_highest_volume_for_each_category/<YearMonth>')
def category_report(YearMonth):
  db = get_db_or_fail()
  cursor = db.cursor()
  sql = utils.get_sqls('state_with_highest_volume_for_each_category.sql')[0]
  cursor.execute(sql)
  summary = cursor.fetchall()

  sql = utils.get_sqls('state_with_highest_volume_for_each_category.sql')[1]
  cursor.execute(sql, (YearMonth, YearMonth,))
  details = cursor.fetchall()
  return render_template('state_with_highest_volume_for_each_category.html',
                         YearMonth=YearMonth, summary= summary, details= details)

