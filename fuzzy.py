import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

class fuzzy:
	def __init__(self):
		self.x_education = np.arange(0, 101, 1)
		self.x_age = np.arange(0, 101, 1)
		self.x_finance = np.arange(0, 101, 1)

		self.edu_low = fuzz.trimf(self.x_education, [0, 0, 40])
		self.edu_med = fuzz.trimf(self.x_education, [0, 40, 100])
		self.edu_high = fuzz.trimf(self.x_education, [40, 100, 100])

		self.age_low = fuzz.trimf(self.x_age, [0, 0, 50])
		self.age_med = fuzz.trimf(self.x_age, [0, 50, 100])
		self.age_high = fuzz.trimf(self.x_age, [50, 100, 100])

		self.fin_low = fuzz.trimf(self.x_finance, [0, 0, 60])
		self.fin_med = fuzz.trimf(self.x_finance, [0, 60, 100])
		self.fin_high = fuzz.trimf(self.x_finance, [60, 100, 100])

	def get_edu_set(self):
		return self.x_education, self.edu_low, self.edu_med, self.edu_high

	def get_age_set(self):
		return self.x_age, self.age_low, self.age_med, self.age_high

	def get_fin_set(self):
		return self.x_finance, self.fin_low, self.fin_med, self.fin_high



