import requests


from .EnumUserAuth import EnumUserAuth
from .Error import Error
from .Network import Network
from .NetworkConfig import NetworkConfig
from .NetworkDeleteStatus import NetworkDeleteStatus
from .NetworkIpAssignmentPool import NetworkIpAssignmentPool
from .NetworkMember import NetworkMember
from .NetworkMemberConfig import NetworkMemberConfig
from .NetworkRelay import NetworkRelay
from .NetworkRule import NetworkRule
from .SystemStatus import SystemStatus
from .User import User

from .client import Client as APIClient


class Client:
    def __init__(self, base_uri="https://my.zerotier.com/api"):
        self.api = APIClient(base_uri)
        