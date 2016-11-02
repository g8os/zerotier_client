import requests

from .network_service import  NetworkService 
from .self_service import  SelfService 
from .status_service import  StatusService 
from .user_service import  UserService 

BASE_URI = "https://my.zerotier.com/api"


class Client:
    def __init__(self):
        self.base_url = BASE_URI
        self.session = requests.Session()
        self.session.headers.update({"Content-Type": "application/json"})
        
        self.network = NetworkService(self)
        self.self = SelfService(self)
        self.status = StatusService(self)
        self.user = UserService(self)
    
    def set_auth_header(self, val):
        ''' set authorization header value'''
        self.session.headers.update({"Authorization":val})