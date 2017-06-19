"""
Auto-generated class for NetworkConfig
"""
from .NetworkIpAssignmentPool import NetworkIpAssignmentPool
from .NetworkRelay import NetworkRelay
from .NetworkRule import NetworkRule

from . import client_support


class NetworkConfig(object):
    """
    auto-generated. don't touch.
    """

    @staticmethod
    def create(authorizedMemberCount=None, clock=None, controllerInstanceId=None, creationTime=None, ipAssignmentPools=None, ipLocalRoutes=None, memberRevisionCounter=None, multicastLimit=None, name=None, nwid=None, private=None, relays=None, revision=None, rules=None, v4AssignMode=None, v6AssignMode=None):
        """
        :type authorizedMemberCount: int
        :type clock: int
        :type controllerInstanceId: str
        :type creationTime: int
        :type ipAssignmentPools: list[NetworkIpAssignmentPool]
        :type ipLocalRoutes: list[str]
        :type memberRevisionCounter: int
        :type multicastLimit: int
        :type name: str
        :type nwid: str
        :type private: bool
        :type relays: list[NetworkRelay]
        :type revision: int
        :type rules: list[NetworkRule]
        :type v4AssignMode: str
        :type v6AssignMode: str
        :rtype: NetworkConfig
        """

        return NetworkConfig(
            authorizedMemberCount=authorizedMemberCount,
            clock=clock,
            controllerInstanceId=controllerInstanceId,
            creationTime=creationTime,
            ipAssignmentPools=ipAssignmentPools,
            ipLocalRoutes=ipLocalRoutes,
            memberRevisionCounter=memberRevisionCounter,
            multicastLimit=multicastLimit,
            name=name,
            nwid=nwid,
            private=private,
            relays=relays,
            revision=revision,
            rules=rules,
            v4AssignMode=v4AssignMode,
            v6AssignMode=v6AssignMode,
        )

    def __init__(self, json=None, **kwargs):
        if json is None and not kwargs:
            raise ValueError('No data or kwargs present')

        class_name = 'NetworkConfig'
        create_error = '{cls}: unable to create {prop} from value: {val}: {err}'
        required_error = '{cls}: missing required property {prop}'

        data = json or kwargs

        property_name = 'authorizedMemberCount'
        val = data.get(property_name)
        if val is not None:
            datatypes = [int]
            try:
                self.authorizedMemberCount = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'clock'
        val = data.get(property_name)
        if val is not None:
            datatypes = [int]
            try:
                self.clock = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'controllerInstanceId'
        val = data.get(property_name)
        if val is not None:
            datatypes = [str]
            try:
                self.controllerInstanceId = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'creationTime'
        val = data.get(property_name)
        if val is not None:
            datatypes = [int]
            try:
                self.creationTime = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'ipAssignmentPools'
        val = data.get(property_name)
        if val is not None:
            datatypes = [NetworkIpAssignmentPool]
            try:
                self.ipAssignmentPools = client_support.list_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'ipLocalRoutes'
        val = data.get(property_name)
        if val is not None:
            datatypes = [str]
            try:
                self.ipLocalRoutes = client_support.list_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'memberRevisionCounter'
        val = data.get(property_name)
        if val is not None:
            datatypes = [int]
            try:
                self.memberRevisionCounter = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'multicastLimit'
        val = data.get(property_name)
        if val is not None:
            datatypes = [int]
            try:
                self.multicastLimit = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'name'
        val = data.get(property_name)
        if val is not None:
            datatypes = [str]
            try:
                self.name = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'nwid'
        val = data.get(property_name)
        if val is not None:
            datatypes = [str]
            try:
                self.nwid = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'private'
        val = data.get(property_name)
        if val is not None:
            datatypes = [bool]
            try:
                self.private = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'relays'
        val = data.get(property_name)
        if val is not None:
            datatypes = [NetworkRelay]
            try:
                self.relays = client_support.list_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'revision'
        val = data.get(property_name)
        if val is not None:
            datatypes = [int]
            try:
                self.revision = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'rules'
        val = data.get(property_name)
        if val is not None:
            datatypes = [NetworkRule]
            try:
                self.rules = client_support.list_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'v4AssignMode'
        val = data.get(property_name)
        if val is not None:
            datatypes = [str]
            try:
                self.v4AssignMode = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'v6AssignMode'
        val = data.get(property_name)
        if val is not None:
            datatypes = [str]
            try:
                self.v6AssignMode = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

    def __str__(self):
        return self.as_json(indent=4)

    def as_json(self, indent=0):
        return client_support.to_json(self, indent=indent)

    def as_dict(self):
        return client_support.to_dict(self)
