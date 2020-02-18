import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

import fuzzy
import plot
import rules

#########################################
# Collect the crisp input from the user #
#########################################

# Global variables,
# this is later filled by the input from the user
age_level = 0
beauty_level = 0
career_level = 0
edu_level = 0
fin_level = 0
politics_level = 0
height_level = 0
weight_level = 0

# User input
print("How old are you?: (21 - 28 yrs old)")
age_level = input()
print("Rate yourself! (out of 10):")
beauty_level = input()
print("How close are you to reaching your dream job?(Enter in percentage):")
career_level = input()
print("Enter education level (0 = No degree, 25 = High School Diploma, 50 = Bachelors, 75 = Masters, 100 = PhD):")
edu_level = input()
print("Enter annual salary (in Thousands):")
fin_level = input()
print("How much do you follow politics? (out of 10):")
politics_level = input()
print("How tall are you? (in cms):")
height_level = input()
print("How much do you weigh? (in lbs):")
weight_level = input()

##############################################################################
# Fuzzifier, make fuzzy sets, generate fuzzy triangular membership functions #
##############################################################################

# Age measured in years from 21-28
age_array = [[21, 21, 23], [21, 25, 28], [25, 28, 28]]
age = fuzzy.fuzzy(21, 29, 1, age_array)

# Beauty measured out of 10
beauty_array = [[0,0,4],[1,5,10],[6,10,10]]
beauty = fuzzy.fuzzy(0, 10, 1, beauty_array)

# Career level measured in percentage of how much is reached
career_array = [[0, 0, 50], [0, 40, 90], [40, 100, 100]]
career = fuzzy.fuzzy(0, 100, 10, career_array)

# Education measured from 0 to 100
edu_array = [[0, 0, 50], [0, 50, 100], [50, 100, 100]]
edu = fuzzy.fuzzy(0, 101, 1, edu_array)

# Financial standing measured in thousands of $ per year
fin_array = [[0, 0, 60], [0, 60, 100], [60, 200, 200]]
fin = fuzzy.fuzzy(0, 201, 1, fin_array)

# Political standing measured out of 10, 10 means follows politics closely, 0 means don't
# We don't want a political nut or someone who doesn't know anything about politics
politics_array = [[0,0,5],[0,5,9],[6,10,10]]
politics = fuzzy.fuzzy(0, 10, 1, politics_array)

# Height measured in cms (Looking for people from 130cms to 200cms)
height_array = [[130,140,160],[140,160,200],[170,200,200]]
height = fuzzy.fuzzy(130, 200, 1, height_array)

# Weight measured in lbs (Looking for people from 120 lbs to 160 lbs)
weight_array = [[100,120,120,130],[120,140,150,160],[140,160,170,200]]
weight = fuzzy.fuzzy(120, 200, 2, weight_array)

# Fuzzy set for the result
# This set specifies, how good of a match it is. Measured in percentage
match_array = [[0, 0, 50], [0, 50, 100], [50, 100, 100]]
match = fuzzy.fuzzy(0, 101, 1, match_array)

######################################################
# Make rules and add them to the intelligence engine #
######################################################

# Memberships
age_mem = age.get_membership(age_level)
beauty_mem = beauty.get_membership(beauty_level)
career_mem = career.get_membership(career_level)
edu_mem = edu.get_membership(edu_level)
fin_mem = fin.get_membership(fin_level)
politics_mem = politics.get_membership(politics_level)
height_mem = height.get_membership(height_level)
weight_mem = weight.get_membership(weight_level)

# Low Match Rule
rule1 = np.fmax(np.fmax(edu_mem[0], fin_mem[0]), age_mem[0])
match_level_low = np.fmin(rule1, match.get_low_set())

# Med Match Rule
rule2 = np.fmax(np.fmax(edu_mem[1], fin_mem[1]), age_mem[1])
match_level_mid = np.fmin(rule2, match.get_med_set())

# High Match Rule
rule3 = np.fmax(np.fmax(edu_mem[2], fin_mem[2]), age_mem[2])
match_level_high = np.fmin(rule3, match.get_high_set())

# Empty array for match level
match_level = np.zeros_like(match.get_fuzzy_range())

######################################################
# Defuzification and collect crisp values for output #
######################################################

aggregated = np.fmax(match_level_low, np.fmax(match_level_mid, match_level_high))

match_amount = fuzz.defuzz(match.get_fuzzy_range(), aggregated, "centroid")
match_activation = fuzz.interp_membership(match.get_fuzzy_range(), aggregated, match_amount)

# Initialize graphs to populate later
plots_a = plot.plot()
plots_b = plot.plot()
plots_c = plot.plot()

# 3 graphs in 1 window
plots_a.set_graph(0, edu.get_set, "Education", ["Low", "Average", "High"])
plots_a.set_graph(1, age.get_set, "Age", ["Young", "Middle-Aged", "Old"])
plots_a.set_graph(2, fin.get_set, "Finance", ["Poor", "Average", "Wealthy"])

# 3 graphs in 1 window
plots_b.set_graph(0, beauty.get_set, "Beauty", ["Ugly", "Average", "Beautiful"])
plots_b.set_graph(1, career.get_set, "Career", ["Haven't started", "In progress", "Acheived"])
plots_b.set_graph(2, politics.get_set, "Politics", ["Not Political", "Somewhat", "Very Political"])

# 3 graphs in 1 window
plots_c.set_graph(0, height.get_set, "Height", ["Short", "Average", "Tall"])
plots_c.set_graph(1, weight.get_set, "Weight", ["Underweight", "Average", "Overweight"])
plots_c.set_graph(2, match.get_set, "Match", ["Low", "Medium", "High"])

# Plot aggregated membership and result
fig, ax0 = plt.subplots(figsize=(8, 2))
ax0.plot(match.get_fuzzy_range(), match_level_low, 'b', linewidth=1, linestyle='--', )
ax0.plot(match.get_fuzzy_range(), match_level_mid, 'g', linewidth=1, linestyle='--')
ax0.plot(match.get_fuzzy_range(), match_level_high, 'r', linewidth=1, linestyle='--')
ax0.fill_between(match.get_fuzzy_range(), match_level, aggregated, facecolor='Orange', alpha=0.7)
ax0.plot([match_amount, match_amount], [0, match_activation], 'k', linewidth=1.5, alpha=0.9)
ax0.set_title('Aggregated membership and result (line)')

print("Match Amount:" + str(match_amount))

plt.tight_layout()
plt.show()
