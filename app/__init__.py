from flask import Flask


def create_app():
  app = Flask(__name__)
  app.config.from_mapping(SECRET_KEY='dev')

  @app.route('/about')
  def hello():
    return 'This is the Phase 3 web app.'

  from . import db
  db.init_app(app)

  from . import auth
  app.register_blueprint(auth.bp)

  from . import summary
  app.register_blueprint(summary.bp)
  app.add_url_rule('/', endpoint='summary')

  from . import city
  app.register_blueprint(city.bp)

  # Register the blueprint of your report here.
  from . import manufacturers_product
  app.register_blueprint(manufacturers_product.bp)

  from . import category
  app.register_blueprint(category.bp)

  from . import actvspredict_revenue_couch_sofa
  app.register_blueprint(actvspredict_revenue_couch_sofa.bp)


  from . import store_revenue_by_year_by_state
  app.register_blueprint(store_revenue_by_year_by_state.bp)

  from . import outdoor_furniture_on_groundhog_day
  app.register_blueprint(outdoor_furniture_on_groundhog_day.bp)

  from . import state_with_highest_volume_for_each_category
  app.register_blueprint(state_with_highest_volume_for_each_category.bp)

  from . import revenue_by_population
  app.register_blueprint(revenue_by_population.bp)

  from . import grand_showcase_store_revenue_comparison
  app.register_blueprint(grand_showcase_store_revenue_comparison.bp)

  from . import grand_showcase_category_comparison
  app.register_blueprint(grand_showcase_category_comparison.bp)

  return app
