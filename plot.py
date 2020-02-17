import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

import fuzzy

class plot:
	def __init__(self):
		self.ax = [None, None, None]
		self.fig, (self.ax[0], self.ax[1], self.ax[2]) = plt.subplots(nrows=3, figsize=(6, 9))

	def set_graph(self, num, function, title, labels):
		xaxis, fuzzy_set = function()

		self.ax[num].plot(xaxis, fuzzy_set[0], "y", linewidth=1, label=labels[0])
		self.ax[num].plot(xaxis, fuzzy_set[1], "c", linewidth=1, label=labels[1])
		self.ax[num].plot(xaxis, fuzzy_set[2], "m", linewidth=1, label=labels[2])
		self.ax[num].set_title(title)
		self.ax[num].legend()

	def get_graphs(self):
		return self.ax[0], self.ax[1], self.ax[2]

