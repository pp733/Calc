""" This is the increment function"""
from calc.history.calculations import Calculations

#the calculator class just contains the methods to calculate
class Calculator:
    """ This is the Calculator class"""
    #the calculator class just calls methods on Calculations class
    @staticmethod
    def get_last_result_value():
        """ This is the gets the result of the calculation"""
        # I made this method so that I don't have more than one action per function
        return Calculations.get_last_calculation_result_value()
    @staticmethod
    def multiply_numbers(tuple_values: tuple):
        """ multiplication number from result and returns a multiplication result object"""
        return Calculations.add_multiplication_calculation(tuple_values)
    @staticmethod
    def subtract_numbers(tuple_values: tuple):
        """ subtract a list of numbers from result and returns a subtraction result object"""
        return Calculations.add_subtraction_calculation(tuple_values)
    @staticmethod
    #tuple allows me to pass in as many values as a I want
    def add_numbers(tuple_values: tuple):
        """ adds list of numbers and returns an addition result object"""
        return Calculations.add_addition_calculation(tuple_values)