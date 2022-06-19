from flask_restful import Resource
from settings import app_info


class PyFinVersion(Resource):

    def get(self):
        return app_info
