from app.controllers.controller import ControllerBase
from flask import render_template

class IndexController(ControllerBase):
    @staticmethod
    def get():
        return render_template('index.html')

class PylintController(ControllerBase):
    @staticmethod
    def get():
        return render_template('pylint.html')

class AAAController(ControllerBase):
    @staticmethod
    def get():
        return render_template('AAA.html')

class OOPController(ControllerBase):
    @staticmethod
    def get():
        return render_template('OOPs.html')

class SOLIDController(ControllerBase):
    @staticmethod
    def get():
        return render_template('SOLID.html')