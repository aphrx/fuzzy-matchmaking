import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

import fuzzy
import plot

edu = fuzzy.fuzzy()
age = fuzzy.fuzzy()
fin = fuzzy.fuzzy()

edu.set_fuzzy_range(0, 101, 1)
age.set_fuzzy_range(0, 101, 1)
fin.set_fuzzy_range(0, 101, 1)

edu_array = [[0, 0, 50], [0, 50, 100], [50, 100, 100]]
age_array = [[0, 0, 40], [0, 40, 100], [40, 100, 100]]
fin_array = [[0, 0, 60], [0, 60, 100], [60, 100, 100]]

edu.set_fuzzy_set(edu_array)
age.set_fuzzy_set(age_array)
fin.set_fuzzy_set(fin_array)

plots = plot.plot()

plots.set_graph(0, edu.get_set, "Education")
plots.set_graph(1, age.get_set, "Age")
plots.set_graph(2, fin.get_set, "Finance")

ax0, ax1, ax2 = plots.get_graphs()

plt.tight_layout()
plt.show()