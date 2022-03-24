from flask import (
  Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from app.auth import login_required
from app.db import get_db_or_fail
from . import utils

bp = Blueprint('outdoor_furniture_on_groundhog_day', __name__)


@bp.route('/outdoor_furniture_on_groundhog_day')
def report():
    db = get_db_or_fail()
    cursor = db.cursor()
    sql = utils.get_sql('outdoor_furniture_on_groundhog_day.sql')
    cursor.execute(sql, ("Outdoor Furniture", "Outdoor Furniture",))
    summary = cursor.fetchall()

    return render_template('outdoor_furniture_on_groundhog_day.html', summary=summary)
