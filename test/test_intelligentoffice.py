import unittest
from datetime import datetime
from unittest.mock import patch, Mock, PropertyMock
import mock.GPIO as GPIO
from mock.SDL_DS3231 import SDL_DS3231
from mock.adafruit_veml7700 import VEML7700
from src.intelligentoffice import IntelligentOffice, IntelligentOfficeError
import unittest
from unittest.mock import patch, MagicMock

class TestIntelligentOffice(unittest.TestCase):

    @patch.object(GPIO, "input")
    def test_check_quadrant_found_worker(self, mock_gpio: Mock ):
        mock_gpio_input.return_value = True
        office = IntelligentOffice()
        result = office.check_quadrant_occupancy(11)
        self.assertTrue(result)
