import json
from src.financial.calculate_loan_repayment_schedule import calculate_loan_repayment_schedule

if __name__ == "__main__":

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

    print(json.dumps(result, indent=2))
