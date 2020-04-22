import unittest
from ahogeotagger import tagger
class SearchTests(unittest.TestCase):
    def setUp(self):
        tagger.init(num_cities=10000)

    def test_city_normal(self):
        search_string =  'As a kid I grew up in New York City'
        expected = [
            (22,29,'New York','New York','United States','US','USA',19354922,40.6943,-73.9249)
        ]

        result = tagger.search(search_string)
        self.assertEqual(result, expected)
    
    def test_city_state_lower_case(self):
        search_string =  'As a kid I grew up in new york, ny'
        expected = [
            (22,33,'New York','New York','United States','US','USA',19354922,40.6943,-73.9249)
        ]        
        result = tagger.search(search_string)
        self.assertEqual(result, expected)

    def test_city_state_country_mixed_case(self):
        search_string =  'As a kid I grew up in new YORK, ny, united STATES'
        expected = [
            (22,48,'New York','New York','United States','US','USA',19354922,40.6943,-73.9249)
        ]
        result = tagger.search(search_string)
        self.assertEqual(result, expected)

    def test_non_us_city_country_mixed_case(self):
        search_string =  'In Pakistan, Lahore is known as a city of gardens'
        expected = [
            (3,10,'','','Pakistan','PK','PAK',0,0,0),
            (13,18,'Lahore','Punjab','Pakistan','PK','PAK',6577000,31.56,74.35),
        ]
        result = tagger.search(search_string)
        self.assertEqual(result, expected)

    def test_non_us_city_combined_case(self):
        search_string =  'Lahore, Pakistan is a historical city'
        expected = [
            (0,15,'Lahore','Punjab','Pakistan','PK','PAK',6577000,31.56,74.35),
        ]
        result = tagger.search(search_string)
        self.assertEqual(result, expected)

    def test_multipe_cities(self):
        search_string = "I grew up in Paris, Berlin, London, UK and Pakistan"
        expected = [
            (13, 17, 'Paris', 'Île-de-France', 'France', 'FR', 'FRA', 9904000, 48.8667, 2.3333),
            (20, 25, 'Berlin', 'Berlin', 'Germany', 'DE', 'DEU', 3406000, 52.5218, 13.4015),
            (28, 33, 'London', 'London, City of', 'United Kingdom', 'GB', 'GBR', 8567000, 51.5, -0.1167),
            (43,50, '','','Pakistan','PK','PAK',0,0,0),        
        ]
        result = tagger.search(search_string)
        print(result)
        self.assertEqual(result, expected)

    def test_full_state_name(self):
        search_string = "Silicon valley is in San Francisco, California"
        result = tagger.search(search_string)
        expected = [
            (21, 45, 'San Francisco', 'California', 'United States','US', 'USA', 3603761, 37.7562, -122.443)
        ]
        self.assertEqual(result,expected)