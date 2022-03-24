from flask import (
  Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from app.auth import login_required
from app.db import get_db_or_fail
from . import utils

bp = Blueprint('actvspredict_revenue_couch_sofa', __name__)


@bp.route('/actvspredict_revenue_couch_sofa')
def report():
  db = get_db_or_fail()
  cursor = db.cursor()
  sql = utils.get_sqls('actvspredict_revenue_couch_sofa.sql')[0]
  cursor.execute(sql)

  summary = cursor.fetchall()

  return render_template('actvspredict_revenue_couch_sofa.html', summary=summary)

