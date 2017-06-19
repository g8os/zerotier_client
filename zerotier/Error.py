"""
Auto-generated class for Error
"""

from . import client_support


class Error(object):
    """
    auto-generated. don't touch.
    """

    @staticmethod
    def create(data=None, id=None, message=None):
        """
        :type data: dict
        :type id: int
        :type message: str
        :rtype: Error
        """

        return Error(
            data=data,
            id=id,
            message=message,
        )

    def __init__(self, json=None, **kwargs):
        if json is None and not kwargs:
            raise ValueError('No data or kwargs present')

        class_name = 'Error'
        create_error = '{cls}: unable to create {prop} from value: {val}: {err}'
        required_error = '{cls}: missing required property {prop}'

        data = json or kwargs

        property_name = 'data'
        val = data.get(property_name)
        if val is not None:
            datatypes = [dict]
            try:
                self.data = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'id'
        val = data.get(property_name)
        if val is not None:
            datatypes = [int]
            try:
                self.id = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'message'
        val = data.get(property_name)
        if val is not None:
            datatypes = [str]
            try:
                self.message = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

    def __str__(self):
        return self.as_json(indent=4)

    def as_json(self, indent=0):
        return client_support.to_json(self, indent=indent)

    def as_dict(self):
        return client_support.to_dict(self)
