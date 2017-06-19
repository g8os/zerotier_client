"""
Auto-generated class for NetworkRule
"""

from . import client_support


class NetworkRule(object):
    """
    auto-generated. don't touch.
    """

    @staticmethod
    def create(action=None, etherType=None, ruleNo=None):
        """
        :type action: str
        :type etherType: int
        :type ruleNo: int
        :rtype: NetworkRule
        """

        return NetworkRule(
            action=action,
            etherType=etherType,
            ruleNo=ruleNo,
        )

    def __init__(self, json=None, **kwargs):
        if json is None and not kwargs:
            raise ValueError('No data or kwargs present')

        class_name = 'NetworkRule'
        create_error = '{cls}: unable to create {prop} from value: {val}: {err}'
        required_error = '{cls}: missing required property {prop}'

        data = json or kwargs

        property_name = 'action'
        val = data.get(property_name)
        if val is not None:
            datatypes = [str]
            try:
                self.action = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'etherType'
        val = data.get(property_name)
        if val is not None:
            datatypes = [int]
            try:
                self.etherType = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

        property_name = 'ruleNo'
        val = data.get(property_name)
        if val is not None:
            datatypes = [int]
            try:
                self.ruleNo = client_support.val_factory(val, datatypes)
            except ValueError as err:
                raise ValueError(create_error.format(cls=class_name, prop=property_name, val=val, err=err))

    def __str__(self):
        return self.as_json(indent=4)

    def as_json(self, indent=0):
        return client_support.to_json(self, indent=indent)

    def as_dict(self):
        return client_support.to_dict(self)
