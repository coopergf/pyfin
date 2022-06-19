from numpy_financial import pmt, ipmt, ppmt


def loan_repayment_schedule(pv, rate, fv, nper, payment_holiday=[], extended=False, accrue_interest=True, periods=12):

    prate = rate/100/periods
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
