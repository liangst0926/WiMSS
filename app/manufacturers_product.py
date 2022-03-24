from flask import (
  Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from app.auth import login_required
from app.db import get_db_or_fail
from . import utils

bp = Blueprint('manufacturers_product', __name__)


@bp.route('/manufacturers_product')
def report():
  db = get_db_or_fail()
  cursor = db.cursor()
  sql = utils.get_sqls('manufacturers_product.sql')[0]
  cursor.execute(sql)

  summary = cursor.fetchall()

  return render_template('manufacturers_product.html', summary=summary)


@bp.route('/manufacturers_product_drill/<manufacturer_name>')
def drill(manufacturer_name):
  db = get_db_or_fail()
  cursor = db.cursor()

  sql = utils.get_sqls('manufacturers_product.sql')[0]
  cursor.execute(sql)
  summary = cursor.fetchall()

  sql = utils.get_sqls('manufacturers_product.sql')[1]
  cursor.execute(sql, (manufacturer_name,))
  details = cursor.fetchall()

  return render_template(
    'manufacturers_product_drill.html',
    manufacturer_name=manufacturer_name,
    summary=summary,
    details=details)
