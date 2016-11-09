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

    def post(self, uri, data, headers, params):
        if type(data) is str:
            return self.session.post(uri, data=data, headers=headers, params=params)
        else:
            return self.session.post(uri, json=data, headers=headers, params=params)

    def put(self, uri, data, headers, params):
        if type(data) is str:
            return self.session.put(uri, data=data, headers=headers, params=params)
        else:
            self.session.put(uri, json=data, headers=headers, params=params)

    def patch(self, uri, data, headers, params):
        if type(data) is str:
            return self.session.patch(uri, data=data, headers=headers, params=params)
        else:
            return self.session.patch(uri, json=data, headers=headers, params=params)