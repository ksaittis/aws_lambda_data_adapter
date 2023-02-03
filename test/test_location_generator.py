import unittest
import sys

sys.path.append("..")
from src.location_generator import generate_location


class TestLocationGenerator(unittest.TestCase):

    def test_extract_values(self):
        payload = {
            "venue_name": "random_venue",
            "building_name": "Main 0",
            "region_name": None,
            "asset_name": None,
            "username": None
        }
        expected_output = "random_venue-Main-0"
        
        self.assertEqual(generate_location(payload), expected_output)

    def test_extract_values_with_empty_values(self):
        payload = {
            "venue_name": "",
            "building_name": None,
            "region_name": None,
            "asset_name": "",
            "username": None
        }
        expected_output = ""
        self.assertEqual(generate_location(payload), expected_output)

    def test_extract_values_with_all_values(self):
        payload = {
            "venue_name": "random_venue",
            "building_name": "Main 0",
            "region_name": "UK",
            "asset_name": "Asset 123",
            "entity_type": "user",
            "username": "john_doe"
        }
        expected_output = "random_venue-Main-0-UK-john_doe"
        self.assertEqual(generate_location(payload), expected_output)