import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

import fuzzy
import plot
from rules import Rules

#########################################
# Collect the crisp input from the user #
#########################################

# universe variables,
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

#########
# RULES #
#########

list_of_matches = []
high_match = []
low_match = []
mid_match = []

# IF Age is LOW AND Beauty is HIGH then Match is HIGH
rule1 = np.fmin(age_mem[0],beauty_mem[2])
rule1_match = np.fmin(rule1, match.get_high_set())
list_of_matches.append(rule1_match)
high_match.append(rule1_match)

# IF Age is MID AND Career is MID then Match is MID
rule2 = np.fmin(age_mem[1],career_mem[1])
rule2_match = np.fmin(rule2, match.get_mid_set())
list_of_matches.append(rule2_match)
mid_match.append(rule2_match)

# IF Education is HIGH OR Career is HIGH then Match is HIGH
rule3 = np.fmax(edu_mem[2], career_mem[2])
rule3_match = np.fmin(rule3, match.get_high_set())
list_of_matches.append(rule3_match)
high_match.append(rule3_match)

# IF Financial is HIGH AND Age is HIGH then Match is HIGH
rule4 = np.fmin(fin_mem[2], age_mem[2])
rule4_match = np.fmin(rule4, match.get_high_set())
list_of_matches.append(rule4_match)
high_match.append(rule4_match)

# IF Height is HIGH OR Weight is MID then Match is HIGH
rule5 = np.fmax(height_mem[2], weight_mem[1])
rule5_match = np.fmin(rule5, match.get_high_set())
list_of_matches.append(rule5_match)
high_match.append(rule5_match)

# IF Politics is HIGH AND Education is LOW then Match is LOW
rule6 = np.fmin(politics_mem[2], edu_mem[0])
rule6_match = np.fmin(rule6, match.get_low_set())
list_of_matches.append(rule6_match)
low_match.append(rule6_match)

# IF career is HIGH AND Financial is HIGH then Match is HIGH
rule7 = np.fmin(career_mem[2], fin_mem[2])
rule7_match = np.fmin(rule7, match.get_high_set())
list_of_matches.append(rule7_match)
high_match.append(rule7_match)

# IF Beauty is LOW AND Weight is HIGH then Match is LOW
rule8 = np.fmin(beauty_mem[0], weight_mem[2])
rule8_match = np.fmin(rule8, match.get_low_set())
list_of_matches.append(rule8_match)
low_match.append(rule8_match)

# IF Politics is LOW OR Beauty is LOW then Match is MID
rule9 = np.fmax(politics_mem[0], beauty_mem[0])
rule9_match = np.fmin(rule9, match.get_mid_set())
list_of_matches.append(rule9_match)
mid_match.append(rule9_match)

# IF Age is LOW AND Financial is HIGH then Match is HIGH
rule10 = np.fmin(age_mem[0], fin_mem[2])
rule10_match = np.fmin(rule10, match.get_high_set())
list_of_matches.append(rule10_match)
high_match.append(rule10_match)

# IF Financial is MID AND Career is MID then Match is MID
rule11 = np.fmin(fin_mem[1], career_mem[1])
rule11_match = np.fmin(rule11, match.get_mid_set())
list_of_matches.append(rule11_match)
mid_match.append(rule11_match)

# IF Politics is HIGH AND Financial is HIGH then Match is MID
rule12 = np.fmin(politics_mem[2], fin_mem[2])
rule12_match = np.fmin(rule12, match.get_mid_set())
list_of_matches.append(rule12_match)
mid_match.append(rule12_match)

# IF Age is LOW AND Weight is LOW AND Financial is HIGH then Match is HIGH
rule13 = np.fmin(np.fmin(age_mem[0], weight_mem[0]), fin_mem[2])
rule13_match = np.fmin(rule13, match.get_high_set())
list_of_matches.append(rule13_match)
high_match.append(rule13_match)

# IF Beauty is HIGH AND Weight is HIGH AND Career is MID then Match is MID
rule14 = np.fmin(np.fmin(beauty_mem[2], weight_mem[2]), career_mem[1])
rule14_match = np.fmin(rule14, match.get_mid_set())
list_of_matches.append(rule14_match)
mid_match.append(rule14_match)

# IF Politics is HIGH OR Education is LOW AND Career is LOW then Match is LOW
rule15 = np.fmin(np.fmax(politics_mem[2], edu_mem[0]), career_mem[0])
rule15_match = np.fmin(rule15, match.get_low_set())
list_of_matches.append(rule15_match)
low_match.append(rule15_match)

# IF Politics is HIGH AND Education is HIGH AND Age is MID then Match is HIGH
rule16 = np.fmin(np.fmin(politics_mem[2], edu_mem[2]), age_mem[1])
rule16_match = np.fmin(rule16, match.get_high_set())
list_of_matches.append(rule16_match)
high_match.append(rule16_match)

# IF Age is MID AND Weight is HIGH AND Beauty is MID AND Education is MID then Match is MID
rule17 =  np.fmin(np.fmin(np.fmin(age_mem[1], weight_mem[2]), beauty_mem[1]), edu_mem[1])
rule17_match = np.fmin(rule17, match.get_mid_set())
list_of_matches.append(rule17_match)
mid_match.append(rule17_match)

# IF Height is LOW or Weight is HIGH AND Education is LOW AND Career is LOW then Match is LOW
rule18 =  np.fmin(np.fmin(np.fmax(height_mem[0], weight_mem[2]), edu_mem[0]), career_mem[0])
rule18_match = np.fmin(rule18, match.get_low_set())
list_of_matches.append(rule18_match)
low_match.append(rule18_match)

# IF Age is LOW or Financial is HIGH AND career is HIGH AND Education is MID then Match is HIGH
rule19 =  np.fmin(np.fmin(np.fmax(age_mem[0], fin_mem[2]), edu_mem[1]), career_mem[2])
rule19_match = np.fmin(rule19, match.get_high_set())
list_of_matches.append(rule19_match)
high_match.append(rule19_match)

# IF Career is LOW or Politics is HIGH AND Education is LOW AND Financial is LOW then match is LOW
rule20 =  np.fmin(np.fmin(np.fmax(career_mem[0], politics_mem[2]), edu_mem[0]), fin_mem[0])
rule20_match = np.fmin(rule20, match.get_low_set())
list_of_matches.append(rule20_match)
low_match.append(rule20_match)

# Empty array for match level
match_level = np.zeros_like(match.get_fuzzy_range())

######################################################
# Defuzification and collect crisp values for output #
######################################################

aggregated = Rules.aggregate(list_of_matches)
high_match_aggregated = Rules.aggregate(high_match)
mid_match_aggregated = Rules.aggregate(mid_match)
low_match_aggregated = Rules.aggregate(low_match)

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

print("Match Amount:" + str(match_amount))

# Plot aggregated membership and result
fig, ax0 = plt.subplots(figsize=(8, 2))
ax0.plot(match.get_fuzzy_range(), low_match_aggregated, 'b', linewidth=1, linestyle='--', )
ax0.plot(match.get_fuzzy_range(), mid_match_aggregated, 'g', linewidth=1, linestyle='--')
ax0.plot(match.get_fuzzy_range(), high_match_aggregated, 'r', linewidth=1, linestyle='--')
ax0.fill_between(match.get_fuzzy_range(), match_level, aggregated, facecolor='Orange', alpha=0.7)
ax0.plot([match_amount, match_amount], [0, match_activation], 'k', linewidth=1.5, alpha=0.9)
ax0.set_title('Aggregated membership and result (line)')
plt.tight_layout()
plt.show()
