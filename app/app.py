"""A simple flask web app"""
from flask import Flask
from app.controllers.index_controller import IndexController, OOPController, PylintController, AAAController, SOLIDController
from app.controllers.calculator_controller import CalculatorController

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route("/", methods=['GET'])
def index_get():
    return IndexController.get()

@app.route("/calculator", methods=['GET'])
def calculator_get():
    return CalculatorController.get()

@app.route("/calculator", methods=['POST'])
def calculator_post():
    return CalculatorController.post()

@app.route("/OOP", methods=['GET'])
def oop_get():
    return OOPController.get()

@app.route("/pylint", methods=['GET'])
def pylint_controller():
    return PylintController.get()

@app.route("/AAA", methods=['GET'])
def aaa_controller():
    return AAAController.get()

@app.route("/SOLID", methods=['GET'])
def solid_controller():
    return SOLIDController.get()
