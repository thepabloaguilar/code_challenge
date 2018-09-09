from flask import abort
from flask_restful import Resource
from flasgger import swag_from

from ..security import encrypt_password, check_encrypted_password, \
    generate_auth_token
from ..model import PostgresSession
from ..model.user import User
from ..parsers import login_parser


class Login(Resource):

    # Verifica se o usuário existe
    # Caso exista a senha no formato de hash é devolvida
    # Caso não exista a request é abortado com o erro 404(Not Found)
    def _get_password_hash(self, username):
        session = PostgresSession()

        user = session.query(
            User.password
        ).select_from(User).\
        filter(User.username == username).one_or_none()

        if not user:
            abort(404, 'Usuario não encontrado')
        return user._asdict()['password']

    # Pega a senha no formato de hash e verifica com a senha
    # enviada na request, se a comparação der sucesso é gerado o token
    # caso a comparação falhe a request é abortada com o erro 401
    @swag_from('../docs/login/login.yml')
    def post(self):
        args = login_parser.parse_args()
        hash_password = self._get_password_hash(args.username)
        if check_encrypted_password(args.password, hash_password):
            return {'token': generate_auth_token(args.username)}
        abort(401, 'Senha Incorreta')
