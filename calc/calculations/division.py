"""This is the addition calculation which is being inherits the
value A and B from calculation class"""

from calc.calculations.calculation import Calculation

class Division(Calculation):
    """ """
    def get_result(self):
        """Get Result is returning the self.value A and B"""
        d1 = enumerate(self.values)
        for i, value in (d1):
            if i != 0:
                dnum = dnum / value
            else:
                dnum = value
        return dnum
