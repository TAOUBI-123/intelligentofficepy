import unittest
from datetime import datetime
from unittest.mock import patch, Mock, PropertyMock
import mock.GPIO as GPIO
from mock.SDL_DS3231 import SDL_DS3231
from mock.adafruit_veml7700 import VEML7700
from src.intelligentoffice import IntelligentOffice, IntelligentOfficeError
import RPi.GPIO as GPIO
import unittest
from unittest.mock import patch, MagicMock
from datetime import datetime

class TestIntelligentOffice(unittest.TestCase):

    @patch.object(GPIO, "input")
    def test_check_quadrant_found_worker(self, mock_gpio: Mock ):
        mock_gpio.return_value = True
        office = IntelligentOffice()
        result = office.check_quadrant_occupancy(11)
        self.assertTrue(result)

    @patch('RPi.GPIO.input')
    def test_check_quadrant_empty(self, mock_gpio_input):
        mock_gpio_input.return_value = False
        office = IntelligentOffice()
        result = office.check_quadrant_occupancy(15)
        self.assertFalse(result)

    @patch('RPi.GPIO.input')
    def test_open_blinds_at_8_weekdays(self, mock_gpio_input):
        self.office = IntelligentOffice()
        self.office.rtc = MagicMock
        self.office.change_servo_angle = MagicMock()
        mock_time = datetime(2024, 1, 1, 8, 0, 0)
        self.office.rtc.read_datetime.return_vale  = mock_time
        self.office.blinds_open = False
        self.office.manage_blinds_based_on_time()
        self.assertTrue(self.office.blinds_open)

    @patch('RPi.GPIO.input')
    def test_close_blinds_at_20_weekdays(self, mock_gpio_input):
        mock_time = datetime(2024, 1, 1, 20, 0, 0)
        self.office.rtc.read_datetime.return_vale = mock_time
        self.office.blinds_open = True
        self.office.manage_blinds_based_on_time()
        self.assertFalse(self.office.blinds_open)

    @patch('RPi.GPIO.input')
    def test_no_action_at_weekdays(self):
        mock_time = datetime(2024, 1, 6, 8, 0, 0)
        self.office.rtc.read_datetime.return_vale = mock_time
        self.office.blinds_open = False
        self.office.manage_blinds_based_on_time()
        self.assertFalse(self.office.blinds_open)


