import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt


class fuzzy:
	def __init__(self, start, end, delta, values):
		self.xaxis = np.arange(start, end, delta)
		self.value = len(values[0])
		self.size = len(values)
		self.set = []
                # trimf = Triangular membership function generator
		if self.value == 3:
			if self.size == 3:
				self.set = [fuzz.trimf(self.xaxis, values[0]),
							fuzz.trimf(self.xaxis, values[1]),
							fuzz.trimf(self.xaxis, values[2])]
			elif self.size == 4:
				self.set = [fuzz.trimf(self.xaxis, values[0]),
							fuzz.trimf(self.xaxis, values[1]),
							fuzz.trimf(self.xaxis, values[2]),
							fuzz.trimf(self.xaxis, values[3])]
		if self.value == 4:
			self.set = [fuzz.trapmf(self.xaxis, values[0]),
						fuzz.trapmf(self.xaxis, values[1]),
						fuzz.trapmf(self.xaxis, values[2])]


	def get_set(self):
		return self.xaxis, self.set

	def get_fuzzy_range(self):
		return self.xaxis

	def get_all_sets(self):
		return self.set

	def get_membership(self, level):
		membership = []
		if self.size == 3:
			membership = [	fuzz.interp_membership(self.xaxis, self.set[0], level),
							fuzz.interp_membership(self.xaxis, self.set[1], level),
							fuzz.interp_membership(self.xaxis, self.set[2], level)]
		if self.size == 4:
			membership = [	fuzz.interp_membership(self.xaxis, self.set[0], level),
							fuzz.interp_membership(self.xaxis, self.set[1], level),
							fuzz.interp_membership(self.xaxis, self.set[2], level),
							fuzz.interp_membership(self.xaxis, self.set[3], level)]

		return membership
