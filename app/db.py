import pymysql
from app import dbconfig
from flask import g
from werkzeug.exceptions import abort


def get_db_or_fail():
  if 'db' not in g:
    try:
      g.db = pymysql.connect(
        host=dbconfig.DB_HOST,
	user=dbconfig.DB_USER,
	password=dbconfig.DB_PASSWORD,
	database=dbconfig.DB_DB)
      return g.db
    except pymysql.Error as e:
      _, message = e.args
      abort(404, "Failed to connect to the database: %s" % message)

  return g.db


def close_db(e=None):
  db = g.pop('db', None)

  if db is not None:
    db.close()


def init_app(app):
  app.teardown_appcontext(close_db)
