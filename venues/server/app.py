from flask import Flask
from flask_bootstrap import Bootstrap
from venues.data.feed_loader import initialise_feed_data


def create_app():
    app = Flask(__name__)
    from venues.server.views import services
    app.register_blueprint(services)
    initialise_feed_data()
    Bootstrap(app)
    return app
