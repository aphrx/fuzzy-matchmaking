import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

import fuzzy

sets = fuzzy.fuzzy()

x_education, edu_low, edu_med, edu_high = sets.get_edu_set()
x_age, age_low, age_med, age_high = sets.get_age_set()
x_finance, fin_low, fin_med, fin_high = sets.get_fin_set()

fig, (ax0, ax1, ax2) = plt.subplots(nrows=3, figsize=(8, 9))

ax0.plot(x_education, edu_low, "y", linewidth=1, label="Low")
ax0.plot(x_education, edu_med, "c", linewidth=1, label="Medium")
ax0.plot(x_education, edu_high, "m", linewidth=1, label="High")
ax0.set_title("Education")
ax0.legend()

ax1.plot(x_age, age_low, "y", linewidth=1, label="Low")
ax1.plot(x_age, age_med, "c", linewidth=1, label="Medium")
ax1.plot(x_age, age_high, "m", linewidth=1, label="High")
ax1.set_title("Age")
ax1.legend()

ax2.plot(x_finance, fin_low, "y", linewidth=1, label="Low")
ax2.plot(x_finance, fin_med, "c", linewidth=1, label="Medium")
ax2.plot(x_finance, fin_high, "m", linewidth=1, label="High")
ax2.set_title("Finance")
ax2.legend()

for ax in (ax0, ax1, ax2):
	ax.spines['top'].set_visible(False)
	ax.spines['right'].set_visible(False)
	ax.get_xaxis().tick_bottom()
	ax.get_yaxis().tick_left()
plt.tight_layout()
plt.show()