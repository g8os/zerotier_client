"""
Auto-generated class for NetworkMember
"""
from .NetworkMemberConfig import NetworkMemberConfig

from . import client_support


class NetworkMember(object):
    """
    auto-generated. don't touch.
    """

    @staticmethod
    def create(annot=None, config=None, networkId=None, nodeId=None, state=None, ui=None):
        """
        :type annot: dict
        :type config: NetworkMemberConfig
        :type networkId: str
        :type nodeId: str
        :type state: int
        :type ui: dict
        :rtype: NetworkMember
        """

        return NetworkMember(
            annot=annot,
            config=config,
            networkId=networkId,
            nodeId=nodeId,
            state=state,
            ui=ui,
        )

    def __init__(self, json=None, **kwargs):
        if json is None and not kwargs:
            raise ValueError('No data or kwargs present')

        class_name = 'NetworkMember'
        create_error = '{cls}: unable to create {prop} from value: {val}: {err}'
        required_error = '{cls}: missing required property {prop}'

        data = json or kwargs

        property_name = 'annot'
        val = data.get(property_name)
        if val is not None:
            datatypes = [dict]
            try:
                self.annot = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'config'
        val = data.get(property_name)
        if val is not None:
            datatypes = [NetworkMemberConfig]
            try:
                self.config = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'networkId'
        val = data.get(property_name)
        if val is not None:
            datatypes = [str]
            try:
                self.networkId = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'nodeId'
        val = data.get(property_name)
        if val is not None:
            datatypes = [str]
            try:
                self.nodeId = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'state'
        val = data.get(property_name)
        if val is not None:
            datatypes = [int]
            try:
                self.state = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'ui'
        val = data.get(property_name)
        if val is not None:
            datatypes = [dict]
            try:
                self.ui = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

    def __str__(self):
        return self.as_json(indent=4)

    def as_json(self, indent=0):
        return client_support.to_json(self, indent=indent)

    def as_dict(self):
        return client_support.to_dict(self)
