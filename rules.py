import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

class Rules:
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

    @staticmethod
    def aggregate(list_of_matches):
        current_max = list_of_matches.pop()
        # get the maximum aggregated array of all the matches
        for item in list_of_matches:
            current_max = np.fmax(current_max, item)
        return current_max
