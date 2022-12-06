from unittest import TestCase
from unittest.mock import MagicMock

from core import ParkingView


def prefixed(text: str):
    return f'controle-estacionamento.core.views.{text}'


class TestParkingView(TestCase):
    def setUp(self):
        self.parking = ParkingView

    def test_get_parkings(self):
        mock_request = MagicMock()

        result = self.parking.get_parkings(mock_request)
        
