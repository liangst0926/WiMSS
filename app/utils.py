from flask import current_app


def get_sql(file_name):
  with current_app.open_resource('sql/' + file_name, "r") as f:
    sql = f.read()
  return sql


def get_sqls(file_name):
  with current_app.open_resource('sql/' + file_name, "r") as f:
    sql = f.read()
  return sql.split(';')
