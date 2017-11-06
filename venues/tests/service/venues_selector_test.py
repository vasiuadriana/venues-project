import unittest

from venues.exceptions import InvalidUserSelectionError
from venues.service.venues_selector import VenuesSelector


class TestVenuesSelector(unittest.TestCase):

    def setUp(self):
        self.mock_feed_data = {
            'users': [
                {
                    "name": "Jon",
                    "wont_eat": ["Fish", "Pasta"],
                    "drinks": ["Cider", "Rum"]
                },
                {
                    "name": "Anna",
                    "wont_eat": ["Eggs", "Pasta"],
                    "drinks": ["Tequila", "Coffee"]
                },
                {
                    "name": "Alina",
                    "wont_eat": ["Oysters", "Pasta"],
                    "drinks": ["Wine"]
                }
            ],
            'venues': [
                {
                    "name": "The Cambridge",
                    "food": ["Fish", "Pasta"],
                    "drinks": ["Cider", "Tequila"]
                },
                {
                    "name": "Italian",
                    "food": ["Fish", "Eggs", "Oysters"],
                    "drinks": ["Wine", "Cider"]
                },
                {
                    "name": "Japanese",
                    "food": ["Fish", "Oysters", "Crab"],
                    "drinks": ["Sake", "Cider", "Coffee"]
                },
            ]
        }
        self.venues_selector = VenuesSelector(self.mock_feed_data)

    def test_select_returns_a_list_of_compatible_venues(self):
        venues = self.venues_selector.select_venues(["Anna", "Jon"])
        self.assertEqual(["Japanese"], venues["safe"])

    def test_select_venues_returns_a_list_of_non_compatible_venues_with_reasons(self):
        venues = self.venues_selector.select_venues(["Anna", "Jon"])
        expected_output = {
            "The Cambridge": {
                "nothing_to_eat": ["Jon"],
                "nothing_to_drink": []
            },
            "Italian": {
                "nothing_to_eat": [],
                "nothing_to_drink": ["Anna"]
            }
        }
        self.assertDictEqual(expected_output, venues["to_avoid"])

    def test_select_venues_returns_an_empty_list_of_compatible_venues_if_no_match(self):
        mock_feed_data = self.mock_feed_data.copy()
        mock_feed_data['users'].append({
            "name": "Michael",
            "wont_eat": ["Fish"],
            "drinks": ["Soft drinks"]
        })
        venues_selector = VenuesSelector(mock_feed_data)
        venues = venues_selector.select_venues(["Anna", "Jon", "Michael"])
        self.assertListEqual([], venues["safe"])

    def test_select_venues_for_users_that_dont_exist_fails(self):
        with self.assertRaises(InvalidUserSelectionError):
            self.venues_selector.select_venues(["Random User Name"])

    def test_select_venues_for_an_empty_list_of_users_fails(self):
        with self.assertRaises(InvalidUserSelectionError):
            self.venues_selector.select_venues([])