from flask_restful import reqparse

login_parser = reqparse.RequestParser()
login_parser.add_argument('username', type=str)
login_parser.add_argument('password', type=str)
