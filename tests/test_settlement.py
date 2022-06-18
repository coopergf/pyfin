import unittest
from src.financial.settlement import calculate_settlement


class TestSettlement(unittest.TestCase):

    def test_calculator_returns(self):

        kwargs = {
            "pv": 18564,
            "rate": 5.56,
            "fv": 3564,
            "nper": 12,
            "holiday": [],
            "extended": False,
            "accrue_interest": True
        }

        response = calculate_settlement(**kwargs)

        self.assertIsNotNone(response)
