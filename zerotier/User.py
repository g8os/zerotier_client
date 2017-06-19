"""
Auto-generated class for User
"""
from .EnumUserAuth import EnumUserAuth

from . import client_support


class User(object):
    """
    auto-generated. don't touch.
    """

    @staticmethod
    def create(auth, authUserId, id, state, type, _type=None, annot=None, config=None, displayName=None, email=None, emailConfirmed=None, globalPermissionMask=None, password=None, paymentProcessorCustomerId=None, permissions=None, tokens=None, ui=None):
        """
        :type _type: str
        :type annot: dict
        :type auth: EnumUserAuth
        :type authUserId: str
        :type config: dict
        :type displayName: str
        :type email: str
        :type emailConfirmed: bool
        :type globalPermissionMask: int
        :type id: str
        :type password: str
        :type paymentProcessorCustomerId: str
        :type permissions: dict
        :type state: int
        :type tokens: dict
        :type type: int
        :type ui: dict
        :rtype: User
        """

        return User(
            _type=_type,
            annot=annot,
            auth=auth,
            authUserId=authUserId,
            config=config,
            displayName=displayName,
            email=email,
            emailConfirmed=emailConfirmed,
            globalPermissionMask=globalPermissionMask,
            id=id,
            password=password,
            paymentProcessorCustomerId=paymentProcessorCustomerId,
            permissions=permissions,
            state=state,
            tokens=tokens,
            type=type,
            ui=ui,
        )

    def __init__(self, json=None, **kwargs):
        if json is None and not kwargs:
            raise ValueError('No data or kwargs present')

        class_name = 'User'
        create_error = '{cls}: unable to create {prop} from value: {val}: {err}'
        required_error = '{cls}: missing required property {prop}'

        data = json or kwargs

        property_name = '_type'
        val = data.get(property_name)
        if val is not None:
            datatypes = [str]
            try:
                self._type = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'annot'
        val = data.get(property_name)
        if val is not None:
            datatypes = [dict]
            try:
                self.annot = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'auth'
        val = data.get(property_name)
        if val is not None:
            datatypes = [EnumUserAuth]
            try:
                self.auth = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))
        else:
            raise ValueError(required_error.format(cls=class_name, prop=property_name))

        property_name = 'authUserId'
        val = data.get(property_name)
        if val is not None:
            datatypes = [str]
            try:
                self.authUserId = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))
        else:
            raise ValueError(required_error.format(cls=class_name, prop=property_name))

        property_name = 'config'
        val = data.get(property_name)
        if val is not None:
            datatypes = [dict]
            try:
                self.config = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'displayName'
        val = data.get(property_name)
        if val is not None:
            datatypes = [str]
            try:
                self.displayName = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'email'
        val = data.get(property_name)
        if val is not None:
            datatypes = [str]
            try:
                self.email = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'emailConfirmed'
        val = data.get(property_name)
        if val is not None:
            datatypes = [bool]
            try:
                self.emailConfirmed = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'globalPermissionMask'
        val = data.get(property_name)
        if val is not None:
            datatypes = [int]
            try:
                self.globalPermissionMask = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'id'
        val = data.get(property_name)
        if val is not None:
            datatypes = [str]
            try:
                self.id = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))
        else:
            raise ValueError(required_error.format(cls=class_name, prop=property_name))

        property_name = 'password'
        val = data.get(property_name)
        if val is not None:
            datatypes = [str]
            try:
                self.password = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'paymentProcessorCustomerId'
        val = data.get(property_name)
        if val is not None:
            datatypes = [str]
            try:
                self.paymentProcessorCustomerId = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'permissions'
        val = data.get(property_name)
        if val is not None:
            datatypes = [dict]
            try:
                self.permissions = client_support.val_factory(val, datatypes)
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
        else:
            raise ValueError(required_error.format(cls=class_name, prop=property_name))

        property_name = 'tokens'
        val = data.get(property_name)
        if val is not None:
            datatypes = [dict]
            try:
                self.tokens = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'type'
        val = data.get(property_name)
        if val is not None:
            datatypes = [int]
            try:
                self.type = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))
        else:
            raise ValueError(required_error.format(cls=class_name, prop=property_name))

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
