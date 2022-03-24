from flask import (
  Blueprint, flash, g, redirect, render_template, request, url_for
)

from app.db import get_db_or_fail
from . import utils

bp = Blueprint('revenue_by_population', __name__)


@bp.route('/revenue_by_population')
def report():
  db = get_db_or_fail()
  cursor = db.cursor()

  sqls = utils.get_sqls('revenue_by_population.sql')
  
  cursor.execute(sqls[0])
  db.commit()
  cursor.execute(sqls[1])
  db.commit()
  cursor.execute(sqls[2])
  data = cursor.fetchall()
  return render_template('revenue_by_population.html', result = data)



