"""
Auto-generated class for SystemStatus
"""
from .User import User

from . import client_support


class SystemStatus(object):
    """
    auto-generated. don't touch.
    """

    @staticmethod
    def create(clock=None, loginMethods=None, online=None, paidPlans=None, smsEnabled=None, stripePublishableKey=None, uptime=None, user=None, version=None):
        """
        :type clock: int
        :type loginMethods: dict
        :type online: bool
        :type paidPlans: dict
        :type smsEnabled: bool
        :type stripePublishableKey: str
        :type uptime: int
        :type user: User
        :type version: str
        :rtype: SystemStatus
        """

        return SystemStatus(
            clock=clock,
            loginMethods=loginMethods,
            online=online,
            paidPlans=paidPlans,
            smsEnabled=smsEnabled,
            stripePublishableKey=stripePublishableKey,
            uptime=uptime,
            user=user,
            version=version,
        )

    def __init__(self, json=None, **kwargs):
        if json is None and not kwargs:
            raise ValueError('No data or kwargs present')

        class_name = 'SystemStatus'
        create_error = '{cls}: unable to create {prop} from value: {val}: {err}'
        required_error = '{cls}: missing required property {prop}'

        data = json or kwargs

        property_name = 'clock'
        val = data.get(property_name)
        if val is not None:
            datatypes = [int]
            try:
                self.clock = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'loginMethods'
        val = data.get(property_name)
        if val is not None:
            datatypes = [dict]
            try:
                self.loginMethods = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'online'
        val = data.get(property_name)
        if val is not None:
            datatypes = [bool]
            try:
                self.online = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'paidPlans'
        val = data.get(property_name)
        if val is not None:
            datatypes = [dict]
            try:
                self.paidPlans = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'smsEnabled'
        val = data.get(property_name)
        if val is not None:
            datatypes = [bool]
            try:
                self.smsEnabled = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'stripePublishableKey'
        val = data.get(property_name)
        if val is not None:
            datatypes = [str]
            try:
                self.stripePublishableKey = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'uptime'
        val = data.get(property_name)
        if val is not None:
            datatypes = [int]
            try:
                self.uptime = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'user'
        val = data.get(property_name)
        if val is not None:
            datatypes = [User]
            try:
                self.user = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'version'
        val = data.get(property_name)
        if val is not None:
            datatypes = [str]
            try:
                self.version = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

    def __str__(self):
        return self.as_json(indent=4)

    def as_json(self, indent=0):
        return client_support.to_json(self, indent=indent)

    def as_dict(self):
        return client_support.to_dict(self)
