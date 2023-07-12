# from unittest import TestCase
from django.test import TestCase
from main.weather import weather


class WeatherTestCase(TestCase):
    def test_true_answer(self):
        result = weather("Minsk")
        self.assertEqual(True, result.ok)

    def test_ok_status(self):
        result = weather("Minsk")
        self.assertEqual(200, result.status_code)
