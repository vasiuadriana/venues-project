import unittest

import os

from venues.constants import VENUES_APP_PATH
from venues.data.feed_loader import load_users_data, load_venues_data


class TestFeedLoader(unittest.TestCase):

    def setUp(self):
        self.test_data_dir = os.path.join(VENUES_APP_PATH, 'tests', 'data', 'feeds')

    def test_loads_users_successfully(self):
        users_feed_path = os.path.join(self.test_data_dir, 'users.json')
        actual_output = load_users_data(users_feed_path)
        expected_output = [
            {
                "name": "John Davis",
                "wont_eat": ["Fish"],
                "drinks": ["Cider", "Rum", "Soft drinks"]
            },
            {
                "name": "Gary Jones",
                "wont_eat": ["Eggs", "Pasta"],
                "drinks": ["Tequila", "Soft drinks", "beer", "Coffee"]
            }
        ]
        self.assertEqual(2, len(actual_output))
        self.assertListEqual(expected_output, actual_output)

    def test_loads_venues_successfully(self):
        venues_feed_path = os.path.join(self.test_data_dir, 'venues.json')
        actual_output = load_venues_data(venues_feed_path)
        expected_output = [
            {
                "name": "El Cantina",
                "food": ["Mexican"],
                "drinks": ["Soft drinks", "Tequila", "Beer"]
            },
            {
                "name": "Twin Dynasty",
                "food": ["Chinese"],
                "drinks": ["Soft Drinks", "Rum", "Beer", "Whisky", "Cider"]
            }
        ]
        self.assertEqual(2, len(actual_output))
        self.assertListEqual(expected_output, actual_output)
