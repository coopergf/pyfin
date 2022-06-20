from numpy_financial import pmt, ipmt, ppmt


def calculate_loan_repayment_schedule(
    present_value,
    rate,
    future_value,
    number_of_payments,
    payment_holiday=None,
    extended=False,
    accrue_interest=True
):
    """Calculate the repayments to be made on a financial agreement.

    The calculator allows for payment holidays to be taken.

    Args:
        present_value (float): Amount of loan / principal.

        rate (float): Interest rate.

        future_value (float): Final payment/balloon amount.

        number_of_payments (int): Term of agreement in months.

        payment_holiday (:obj:`list` of :obj:`int`): Periods of
            holiday payment e.g. no payment made on months [2,3].

        extended (bool): If a holiday payment is taken, do we allow
            the term of the contract to be extended.

        accrue_interest (bool): During a holiday payment should the
            loan / principal be increased by the amount of interest
            payable on the loan / principal for that period.

    Returns:
        :obj:`list` of :obj:`dict`: loan repayment schedule.

        Example:

            [
                {
                    "month": 0,
                    "present_value": 18564,
                    "rate": 5.56,
                    "future_value": 3564,
                    "number_of_payments": 12,
                    "payment_amount": 1304.4780587544135,
                    "interest": 86.0132,
                    "paid": 1218.4648587544134,
                    "balance": 17345.535141245586
                },
                ...
            ]

    """

    # annual rate divided by the number of payment periods
    # TODO: allow for variations?
    prate = rate/100/12
    schedule = []
    balance = present_value
    repayment = pmt(prate, number_of_payments, -present_value, future_value)
    add_months = (len(payment_holiday) if extended else 0)
    revised_term = number_of_payments + add_months

    for month in range(revised_term):

        period = {
            'month': month,
            'present_value': present_value,
            'rate': rate,
            'future_value': future_value,
            'number_of_payments': number_of_payments,
            'pmt': repayment
        }

        interest_payment = ipmt(
            prate,
            1,
            number_of_payments-month,
            -balance,
            future_value
        )

        if month in payment_holiday:
            period['pmt'] = paid = 0
            balance += interest_payment if accrue_interest else 0
            number_of_payments += 1 if extended else 0
            repayment = pmt(
                prate,
                number_of_payments - (month+1),
                -balance,
                future_value
            )
        else:
            paid = ppmt(
                prate,
                1,
                number_of_payments - month,
                -balance,
                future_value
            )

        balance -= paid

        period['interest'] = float(interest_payment)
        period['paid'] = paid
        period['balance'] = balance

        schedule.append(period)

    return schedule
