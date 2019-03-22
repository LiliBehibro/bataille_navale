import json
import math
import matplotlib.pyplot as plt

# creation de table
class Agent:
    def say_hello(self, first_name):
        return "Bien le Bonjour" + first_name+" !"

    def __init__(self, **agent_attributes):
        for attr_name, attr_value in agent_attributes.items():
            setattr(self,attr_name, attr_value
