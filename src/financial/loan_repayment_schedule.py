from numpy_financial import pmt, ipmt, ppmt


def loan_repayment_schedule(pv, rate, fv, nper, payment_holiday=[], extended=False, accrue_interest=True):
    """Calculate the repayments to be made on a financial agreement.

    The calculator allows for payment holidays to be taken.

    Args:
        pv (float): Present Value / amount of loan / principal.
        rate (float): Interest rate.
        fv (float): Future Value / balloon amount.
        nper (int): Notional Period / term of agreement in months.
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
                    "pv": 18564,
                    "rate": 5.56,
                    "fv": 3564,
                    "nper": 12,
                    "pmt": 1304.4780587544135,
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
    balance = pv
    repayment = pmt(prate, nper, -pv, fv)
    revised_term = nper + (len(payment_holiday) if extended else 0)

    for i in range(revised_term):

        period = {
            'month': i,
            'pv': pv,
            'rate': rate,
            'fv': fv,
            'nper': nper,
            'pmt': repayment
        }

        interest_payment = ipmt(prate, 1, nper-i, -balance, fv)

        if i in payment_holiday:
            period['pmt'] = paid = 0
            balance += interest_payment if accrue_interest else 0
            nper += 1 if extended else 0
            repayment = pmt(prate, nper-(i+1), -balance, fv)
        else:
            paid = ppmt(prate, 1, nper-i, -balance, fv)

        balance -= paid

        period['interest'] = float(interest_payment)
        period['paid'] = paid
        period['balance'] = balance

        schedule.append(period)

    return schedule
