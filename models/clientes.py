# -*- coding:utf-8 -*-
import settings
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import BadSignature, SignatureExpired

class Cliente(object):
    FILD_SIGNATURE = ("username",)
    
    def __init__(self,username):
        self.username = username
    
    def generar_token(self,expiration):
        return Cliente.generar_auth_token(user=self,expiration=expiration)
        
    def stringify(self):
        return self.__dict__
    
    @staticmethod
    def login(username,password):
        return Cliente(username)
    
    @staticmethod
    def generar_auth_token(user=None,expiration=60*10):
        secrey_key = settings.SECRET_KEY
        s = Serializer(secrey_key,expires_in=expiration)
        data = { c:user.__getattribute__(c) for c in Cliente.FILD_SIGNATURE }
        return s.dumps({"cliente":data})
    
    @staticmethod
    def verificar_auth_token(token):
        s = Serializer(settings.SECRET_KEY)
        try:
            data = s.loads(token)
        except SignatureExpired as e:
            print "SignatureExpired:",e
            return None
        except BadSignature as e:
            print "BadSignature:",e
            return None
        data_cliente = data["cliente"]

        return data_cliente