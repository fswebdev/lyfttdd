import unittest
from serviceable import CarriganTire


class CarriganTireTest(unittest.TestCase):

    def test_needs_service_when_wear_value_is_0_9(self):
        tire_wear_array = [0.9, 0.5, 0.3, 0.1]
        tire = CarriganTire(tire_wear_array)
        self.assertTrue(tire.needs_service())

    def test_needs_service_when_all_wear_values_are_less_than_0_9(self):
        tire_wear_array = [0.8, 0.5, 0.3, 0.1]
        tire = CarriganTire(tire_wear_array)
        self.assertFalse(tire.needs_service())