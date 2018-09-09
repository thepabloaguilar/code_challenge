import datetime
import jwt

from functools import wraps
from flask import abort, request
from passlib.context import CryptContext


_pwd_context = CryptContext(
            schemes=['pbkdf2_sha256'])


# Faz a encriptação da senha
def encrypt_password(password):
    return _pwd_context.encrypt(password)


# Faz a verificação da senha com o Hash gerado anteriormente
def check_encrypted_password(password, hashed):
    return _pwd_context.verify(password, hashed)


# Gera um Token JWT com expiração de 1 hora
def generate_auth_token(username):
    try:
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1),
            'iat': datetime.datetime.utcnow(),
            'sub': {
                'username': username,
            }
        }
        token = jwt.encode(payload, 'CHAVE_DE_CRIPTOGRAFIA', algorithm='HS256')
        return token.decode()
    except Exception as e:
        return e


# Verifica a autenticidade do token e retorna o payload
def decode_auth_token(token):
    try:
        payload = jwt.decode(token, 'CHAVE_DE_CRIPTOGRAFIA')
        return payload['sub']
    except jwt.ExpiredSignatureError:
        abort(401, 'Token Invalido ou Expirado')
    except jwt.InvalidSignatureError:
        abort(401, 'Token Invalido ou Expirado')
    except jwt.exceptions.DecodeError:
        abort(401, 'Token Invalido ou Expirado')


# Decorator para verificar a autenticidade do Token enviado
# no HEADER na request
def auth_token_required(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        token = request.headers.get('Token', None)

        if not token:
            abort(403, 'Token não especificado no header')
        
        informations = decode_auth_token(token)
        return func(*args, **kwargs)
    return decorated
