"""
Auto-generated class for NetworkMemberConfig
"""

from . import client_support


class NetworkMemberConfig(object):
    """
    auto-generated. don't touch.
    """

    @staticmethod
    def create(activeBridge=None, address=None, authorized=None, clock=None, identity=None, ipAssignments=None, memberRevision=None, nwid=None):
        """
        :type activeBridge: bool
        :type address: str
        :type authorized: bool
        :type clock: int
        :type identity: str
        :type ipAssignments: list[str]
        :type memberRevision: int
        :type nwid: str
        :rtype: NetworkMemberConfig
        """

        return NetworkMemberConfig(
            activeBridge=activeBridge,
            address=address,
            authorized=authorized,
            clock=clock,
            identity=identity,
            ipAssignments=ipAssignments,
            memberRevision=memberRevision,
            nwid=nwid,
        )

    def __init__(self, json=None, **kwargs):
        if json is None and not kwargs:
            raise ValueError('No data or kwargs present')

        class_name = 'NetworkMemberConfig'
        create_error = '{cls}: unable to create {prop} from value: {val}: {err}'
        required_error = '{cls}: missing required property {prop}'

        data = json or kwargs

        property_name = 'activeBridge'
        val = data.get(property_name)
        if val is not None:
            datatypes = [bool]
            try:
                self.activeBridge = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'address'
        val = data.get(property_name)
        if val is not None:
            datatypes = [str]
            try:
                self.address = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'authorized'
        val = data.get(property_name)
        if val is not None:
            datatypes = [bool]
            try:
                self.authorized = client_support.val_factory(val, datatypes)
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

        property_name = 'identity'
        val = data.get(property_name)
        if val is not None:
            datatypes = [str]
            try:
                self.identity = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'ipAssignments'
        val = data.get(property_name)
        if val is not None:
            datatypes = [str]
            try:
                self.ipAssignments = client_support.list_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'memberRevision'
        val = data.get(property_name)
        if val is not None:
            datatypes = [int]
            try:
                self.memberRevision = client_support.val_factory(val, datatypes)
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

    def __str__(self):
        return self.as_json(indent=4)

    def as_json(self, indent=0):
        return client_support.to_json(self, indent=indent)

    def as_dict(self):
        return client_support.to_dict(self)
