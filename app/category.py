from flask import (
  Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from app.auth import login_required
from app.db import get_db_or_fail
from . import utils

bp = Blueprint('category', __name__)


@bp.route('/category')
def report():
  db = get_db_or_fail()
  cursor = db.cursor()
  sql = utils.get_sqls('category.sql')[0]
  cursor.execute(sql)

  summary = cursor.fetchall()

  return render_template('category.html', summary=summary)

