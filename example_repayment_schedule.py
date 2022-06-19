import json
from src.financial.loan_repayment_schedule import loan_repayment_schedule

if __name__ == "__main__":

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

    print(json.dumps(result, indent=2))
