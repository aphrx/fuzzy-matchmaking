import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt


class fuzzy:
	def __init__(self, low, med, high, values):
		self.xaxis = np.arange(low, med, high)
		self.set = [None, None, None]
		self.set[0] = fuzz.trimf(self.xaxis, [values[0][0], values[0][1], values[0][2]])
		self.set[1] = fuzz.trimf(self.xaxis, [values[1][0], values[1][1], values[1][2]])
		self.set[2] = fuzz.trimf(self.xaxis, [values[2][0], values[2][1], values[2][2]])

	def get_set(self):
		return self.xaxis, self.set

	def set_fuzzy_range(self, low, med, high):
		self.xaxis = None

	def get_fuzzy_range(self):
		return self.xaxis

	def get_low_set(self):
		return self.set[0]
	
	def get_med_set(self):
		return self.set[1]
	
	def get_high_set(self):
		return self.set[2]

	def set_low_set(self, values):
		self.set[0] = fuzz.trimf(self.xaxis, values[0], values[1], values[2])

	def set_med_set(self, values):
		self.set[1] = fuzz.trimf(self.xaxis, values[0], values[1], values[2])

	def set_high_set(self, values):
		self.set[2] = fuzz.trimf(self.xaxis, values[0], values[1], values[2])

