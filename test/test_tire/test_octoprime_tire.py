import unittest
from serviceable import OctoprimeTire


class OctoprimeTireTest(unittest.TestCase):

    def test_needs_service_when_wear_sum_is_greater_than_or_equal_to_3(self):
        tire_wear_array = [0.8, 0.8, 0.5, 0.9]
        tire = OctoprimeTire(tire_wear_array)
        self.assertTrue(tire.needs_service())

    def test_needs_service_when_wear_sum_is_less_than_3(self):
        tire_wear_array = [0.5, 0.3, 0.2, 0.1]
        tire = OctoprimeTire(tire_wear_array)
        self.assertFalse(tire.needs_service())

    def test_needs_service_with_empty_wear_array(self):
        tire_wear_array = []
        tire = OctoprimeTire(tire_wear_array)
        self.assertFalse(tire.needs_service())