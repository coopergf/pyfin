import unittest
from src.financial.loan_repayment_schedule import loan_repayment_schedule


class TestLoanRepaymentShedule(unittest.TestCase):

    def test_calculator_returns(self):
        '''Some validation of the response.'''

        finance_agreement = {
            "pv": 18564,
            "rate": 5.56,
            "fv": 3564,
            "nper": 12,
            "payment_holiday": [],
            "extended": False,
            "accrue_interest": True
        }

        result = loan_repayment_schedule(**finance_agreement)

        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 12)

    def test_calculator_extends(self):
        '''Length should match term/nper + 
        holiday periods because we extended'''

        finance_agreement = {
            "pv": 18564,
            "rate": 5.56,
            "fv": 3564,
            "nper": 12,
            "payment_holiday": [3, 4, 5],
            "extended": True,
            "accrue_interest": True
        }

        result = loan_repayment_schedule(**finance_agreement)

        self.assertEqual(len(result), 15)

    def test_calculator_does_not_extend(self):
        '''Length should match term/nper because
        we extended are not extending.'''

        finance_agreement = {
            "pv": 18564,
            "rate": 5.56,
            "fv": 3564,
            "nper": 12,
            "payment_holiday": [3, 4, 5],
            "extended": False,
            "accrue_interest": True
        }

        result = loan_repayment_schedule(**finance_agreement)

        self.assertEqual(len(result), 12)
