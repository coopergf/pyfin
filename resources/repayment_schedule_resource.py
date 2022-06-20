from flask_restful import reqparse
from flask_restful import Resource
from src.financial.calculate_loan_repayment_schedule import calculate_loan_repayment_schedule

parser = reqparse.RequestParser(bundle_errors=True)

parser.add_argument('present_value', type=float, required=True,
                    help='loan amount')

parser.add_argument('rate', type=float, required=True,
                    help='interest rate')

parser.add_argument('future_value', type=float, required=True,
                    help='final payment / balloon')

parser.add_argument('number_of_payments', type=int, required=True,
                    help='term of agreement (in months)')

parser.add_argument('payment_holiday', type=str, required=True,
                    help='expecting csv string of integers e.g. "2,3,4"')

parser.add_argument('extended', type=bool, required=True,
                    help='does the payment holiday include an extension')

parser.add_argument('accrue_interest', type=bool, required=True,
                    help='during a payment holiday should we accrue interest')

parser.add_argument('month', type=bool,
                    help='optional argument for returning a single month')


def parse_holiday_string(holstring):
    if holstring:
        return [int(i) for i in holstring.split(',')]
    return []


class RepaymentScheduleResource(Resource):

    def get(self):

        args = parser.parse_args()

        args['payment_holiday'] = parse_holiday_string(args['payment_holiday'])

        month = int(args.pop('month', 0) or 0)

        profile = calculate_loan_repayment_schedule(**args)

        for m in profile:
            m['month'] += 1

        return profile[month] if month else profile
