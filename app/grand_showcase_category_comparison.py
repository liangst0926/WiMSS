from flask import (
  Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from app.auth import login_required
from app.db import get_db_or_fail
from . import utils

bp = Blueprint('grand_showcase_category_comparison', __name__)


@bp.route('/grand_showcase_category_comparison')
def report():
  db = get_db_or_fail()
  cursor = db.cursor()
  sql = utils.get_sqls('grand_showcase_category_comparison.sql')[0]
  cursor.execute(sql)

  summary = cursor.fetchall()

  return render_template('grand_showcase_category_comparison.html', summary=summary)


@bp.route('/grand_showcase_category_comparison_drill/<category_name>')
def drill(category_name):
  db = get_db_or_fail()
  cursor = db.cursor()

  sql = utils.get_sqls('grand_showcase_category_comparison.sql')[0]
  cursor.execute(sql)
  summary = cursor.fetchall()

  sql = utils.get_sqls('grand_showcase_category_comparison.sql')[1]
  cursor.execute(sql, (category_name,))
  details = cursor.fetchall()

  return render_template(
    'grand_showcase_category_comparison_drill.html',
    category_name=category_name,
    summary=summary,
    details=details)

