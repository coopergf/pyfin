from numpy_financial import pmt, ipmt, ppmt


def calculate_settlement(pv, rate, fv, nper, holiday=[], extended=False, accrue_interest=True):

    prate = rate/100/12
    profile = []
    balance = pv
    repayment = pmt(prate, nper, -pv, fv)
    revised_term = nper + (len(holiday) if extended else 0)

    for i in range(revised_term):

        profile.append({
            'month': i, 'pv': pv, 'rate': rate, 'fv': fv, 'nper': nper, 'pmt': repayment
        })

        interest_payment = ipmt(prate, 1, nper-i, -balance, fv)

        if holiday and i in holiday:
            profile[i]['pmt'] = paid = 0
            balance += interest_payment if accrue_interest else 0
            nper += 1 if extended else 0
            repayment = pmt(prate, nper-(i+1), -balance, fv)
        else:
            paid = ppmt(prate, 1, nper-i, -balance, fv)

        balance -= paid
        profile[i]['interest'] = float(interest_payment)
        profile[i]['paid'] = paid
        profile[i]['balance'] = balance

    return profile
