#!/usr/bin/python3
"""12. My integer"""


class MyInt(int):
    """Class called MyInt"""
    def __eq__(self, value):
        """Override == opeartor with !="""
        return self.real != value

    def __ne__(self, value):
        """Override != operator with =="""
        return self.real == value
