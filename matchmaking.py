import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

import fuzzy
import plot
import rules

edu = fuzzy.fuzzy()
age = fuzzy.fuzzy()
fin = fuzzy.fuzzy()
match = fuzzy.fuzzy()

edu_level = 0
age_level = 0
fin_level = 0

edu.set_fuzzy_range(0, 101, 1)
age.set_fuzzy_range(0, 101, 1)
fin.set_fuzzy_range(0, 201, 1)
match.set_fuzzy_range(0, 101, 1)

edu_array = [[0, 0, 50], [0, 50, 100], [50, 100, 100]]
age_array = [[0, 0, 25], [0, 25, 50], [25, 100, 100]]
fin_array = [[0, 0, 60], [0, 60, 100], [60, 200, 200]]
match_array = [[0, 0, 50], [0, 50, 100], [50, 100, 100]]

edu.set_fuzzy_set(edu_array)
age.set_fuzzy_set(age_array)
fin.set_fuzzy_set(fin_array)
match.set_fuzzy_set(match_array)

plots = plot.plot()

plots.set_graph(0, edu.get_set, "Education")
plots.set_graph(1, age.get_set, "Age")
plots.set_graph(2, fin.get_set, "Finance")
plots.set_graph(3, match.get_set, "Match")

ax0, ax1, ax2, ax3 = plots.get_graphs()


# Rule Application

#edu_rule = rules.rules()
#edu_rule.set_rule(edu.get_fuzzy_range(), edu.get_low_set(), edu.get_med_set(), edu.get_high_set(), 60)
#edu_level_low, edu_level_med, edu_level_high = edu_rule.get_rule()

print("Enter education level (0 = No degree, 25 = High School Diploma, 50 = Bachelors, 75 = Masters, 100 = PhD):")
edu_level = input()

print("Enter age:")
age_level = input()

print("Enter annual salary (in Thousands):")
fin_level = input()


edu_level_low = fuzz.interp_membership(edu.get_fuzzy_range(), edu.get_low_set(), edu_level)
edu_level_med = fuzz.interp_membership(edu.get_fuzzy_range(), edu.get_med_set(), edu_level)
edu_level_high = fuzz.interp_membership(edu.get_fuzzy_range(), edu.get_high_set(), edu_level)

age_level_low = fuzz.interp_membership(age.get_fuzzy_range(), age.get_low_set(), age_level)
age_level_med = fuzz.interp_membership(age.get_fuzzy_range(), age.get_med_set(), age_level)
age_level_high = fuzz.interp_membership(age.get_fuzzy_range(), age.get_high_set(), age_level)

fin_level_low = fuzz.interp_membership(fin.get_fuzzy_range(), fin.get_low_set(), fin_level)
fin_level_med = fuzz.interp_membership(fin.get_fuzzy_range(), fin.get_med_set(), fin_level)
fin_level_high = fuzz.interp_membership(fin.get_fuzzy_range(), fin.get_high_set(), fin_level)

# Low Match Rule
rule1 = np.fmax(np.fmax(edu_level_low, fin_level_low), age_level_low)
match_level_low = np.fmin(rule1, match.get_low_set())

# Med Match Rule
rule2 = np.fmax(np.fmax(edu_level_med, fin_level_med), age_level_med)
match_level_mid = np.fmin(rule2, match.get_med_set())

# High Match Rule
rule3 = np.fmax(np.fmax(edu_level_high, fin_level_high), age_level_high)
match_level_high = np.fmin(rule3, match.get_high_set())

match_level = np.zeros_like(match.get_fuzzy_range())

#fig, ax0 = plt.subplots(figsize=(8, 3))
#ax0.fill_between(match.get_fuzzy_range(), match_level, match_level_low, facecolor='b', alpha=0.7)
#ax0.plot(match.get_fuzzy_range(), match_level_low, 'b', linewidth=0.5, linestyle='--', )
#ax0.fill_between(match.get_fuzzy_range(), match_level, match_level_mid, facecolor='g', alpha=0.7)
#ax0.plot(match.get_fuzzy_range(), match_level_mid, 'g', linewidth=0.5, linestyle='--')
#ax0.fill_between(match.get_fuzzy_range(), match_level, match_level_high, facecolor='r', alpha=0.7)
#ax0.plot(match.get_fuzzy_range(), match_level_high, 'r', linewidth=0.5, linestyle='--')
#ax0.set_title('Output membership activity')



# Defuzification
aggregated = np.fmax(match_level_low, np.fmax(match_level_mid, match_level_high))

match_amount = fuzz.defuzz(match.get_fuzzy_range(), aggregated, "centroid")
match_activation = fuzz.interp_membership(match.get_fuzzy_range(), aggregated, match_amount)

fig, ax0 = plt.subplots(figsize=(8, 3))
ax0.plot(match.get_fuzzy_range(), match_level_low, 'b', linewidth=1, linestyle='--', )
ax0.plot(match.get_fuzzy_range(), match_level_mid, 'g', linewidth=1, linestyle='--')
ax0.plot(match.get_fuzzy_range(), match_level_high, 'r', linewidth=1, linestyle='--')
ax0.fill_between(match.get_fuzzy_range(), match_level, aggregated, facecolor='Orange', alpha=0.7)
ax0.plot([match_amount, match_amount], [0, match_activation], 'k', linewidth=1.5, alpha=0.9)
ax0.set_title('Aggregated membership and result (line)')

print(match_amount)

plt.tight_layout()
plt.show()