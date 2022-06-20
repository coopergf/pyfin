import unittest
from src.financial.calculate_loan_repayment_schedule import calculate_loan_repayment_schedule


class TestLoanRepaymentShedule(unittest.TestCase):

    def test_calculator_returns(self):
        '''Response validation.'''

        finance_agreement = {
            "present_value": 18564,
            "rate": 5.56,
            "future_value": 3564,
            "number_of_payments": 12,
            "payment_holiday": [],
            "extended": False,
            "accrue_interest": True
        }

        result = calculate_loan_repayment_schedule(**finance_agreement)

        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 12)

    def test_calculator_extends(self):
        '''Length should match term/number_of_payments + 
        holiday periods because we extended'''

        finance_agreement = {
            "present_value": 18564,
            "rate": 5.56,
            "future_value": 3564,
            "number_of_payments": 12,
            "payment_holiday": [3, 4, 5],
            "extended": True,
            "accrue_interest": True
        }

        result = calculate_loan_repayment_schedule(**finance_agreement)

        self.assertEqual(len(result), 15)

    def test_calculator_does_not_extend(self):
        '''Length should match term/number_of_payments because
        we extended are not extending.'''

        finance_agreement = {
            "present_value": 18564,
            "rate": 5.56,
            "future_value": 3564,
            "number_of_payments": 12,
            "payment_holiday": [3, 4, 5],
            "extended": False,
            "accrue_interest": True
        }

        result = calculate_loan_repayment_schedule(**finance_agreement)

        self.assertEqual(len(result), 12)
