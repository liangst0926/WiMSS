from flask import (
  Blueprint, flash, g, redirect, render_template, request, url_for
)

from app.db import get_db_or_fail
from . import utils

bp = Blueprint('grand_showcase_store_revenue_comparison', __name__)


@bp.route('/grand_showcase_store_revenue_comparison')
def report():
  db = get_db_or_fail()
  cursor = db.cursor()
  sqls = utils.get_sqls('grand_showcase_store_revenue_comparison.sql')
  data = []
  for i,sql in enumerate(sqls[:-1:]):
    cursor.execute(sql)
    if i <= 6:      
      db.commit()
    else:
      data.append(cursor.fetchall())  
  return render_template('grand_showcase_store_revenue_comparison.html', result = data)  
     



