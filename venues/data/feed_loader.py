import json
import os

from venues.constants import VENUES_APP_PATH, USERS_FEED_NAME, VENUES_FEED_NAME

FEED_DATA = None


def load_users_data(user_feed_path):
    return _load_feed(user_feed_path)


def load_venues_data(venues_feed_path):
    return _load_feed(venues_feed_path)


def initialise_feed_data():
    global FEED_DATA
    FEED_DATA = {
        'users': load_users_data(os.path.join(VENUES_APP_PATH, 'data', 'feeds', USERS_FEED_NAME)),
        'venues': load_venues_data(os.path.join(VENUES_APP_PATH, 'data', 'feeds', VENUES_FEED_NAME))
    }


def _load_feed(feed_path):
    with open(feed_path) as f:
        return json.loads(f.read())