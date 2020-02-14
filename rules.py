import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

class rules:
    def __init__(self):
        self.range = None
        self.set = [None, None, None]
        self.low = None
        self.mid = None
        self.high = None

    def set_rule(self, range, seta, setb, setc, i):
        self.low = fuzz.interp_membership(range, seta, i)
        self.mid = fuzz.interp_membership(range, setb, i)
        self.high = fuzz.interp_membership(range, setc, i)

    def get_rule(self):
        return self.low, self.mid, self.high