import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

class fuzzy:
	def __init__(self):
		self.xaxis = None
		self.set = [None, None, None]

	def get_set(self):
		return self.xaxis, self.set

	def set_fuzzy_range(self, low, med, high):
		self.xaxis = np.arange(low, med, high)

	def set_fuzzy_set(self, values):
		self.set[0] = fuzz.trimf(self.xaxis, [values[0][0], values[0][1], values[0][2]])
		self.set[1] = fuzz.trimf(self.xaxis, [values[1][0], values[1][1], values[1][2]])
		self.set[2] = fuzz.trimf(self.xaxis, [values[2][0], values[2][1], values[2][2]])




