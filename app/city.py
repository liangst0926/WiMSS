from flask import (
  Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from app.auth import login_required
from app.db import get_db_or_fail
from . import utils

bp = Blueprint('city', __name__)


@bp.route('/cities')
def cities():
  db = get_db_or_fail()
  cursor = db.cursor()
  sql = utils.get_sqls('summary.sql')[7]
  cursor.execute(sql)
  cities = cursor.fetchall()
  return render_template('cities.html', cities=cities)



def get_city(state, city_name):
  db = get_db_or_fail()
  cursor = db.cursor()
  sql = utils.get_sqls('summary.sql')[8]
  cursor.execute(sql, (state, city_name))
  city = cursor.fetchone()

  if city is None:
    abort(404, f"City {city_name}, {state} doesn't exist.")

  return city


@bp.route('/update_city_population/<state>/<city_name>', methods=('GET', 'POST'))
@login_required
def update_city_population(state, city_name):
  city = get_city(state, city_name)

  if request.method == 'POST':
    city_population = request.form['city_population']
    error = None

    if not city_population:
      error = 'City population is required.'
    else:
      try:
        population = int(city_population)
        if population <= 0:
          error = 'City population must be positive.'
      except ValueError:
        error = 'City population must be an integer.'

    if error is not None:
      flash(error)
    else:
      db = get_db_or_fail()
      cursor = db.cursor()
      sql = utils.get_sqls('summary.sql')[9]
      cursor.execute(sql, (city_population, city_name, state))
      db.commit()
      return redirect(url_for('city.cities'))

  return render_template('update_city_population.html', state=state, city_name=city_name, population=city[2])
