from flask import Flask
from flask_restful import Api
from resources.version import PyFinVersion
from resources.repayment_schedule_resource import RepaymentScheduleResource

app = Flask(__name__)
api = Api(app)

api.add_resource(PyFinVersion, '/', '/version')
api.add_resource(RepaymentScheduleResource, '/repayment/schedule')

if __name__ == '__main__':
    app.run(debug=True)
