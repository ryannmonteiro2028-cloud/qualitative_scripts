#monteiro_compmethods_week5_homework.py

# author: ryann monteiro
# course: computational methods
# week: 5
# date: 2025-10-17
# description: introductory problem set (food-studies context)

# 1. assign a string
primary_theme = "food sovereignty"

# 2. assign a float
primary_theme = 27.4  # average number of market visitors per observation hour
print("#2 primary_theme:", primary_theme, type(primary_theme))


# 3. assign two integers with an operator
total_sites = 12 + 5 #urban gardens + farmers markets
print("#3 total_sites:", total_sites)

# 4. assign concatenated strings
report_title = "Qualitative Memo: " + "Community Food Practices"
print("#4 report_title:", report_title)

# 5. integer + string (convert integer)
interview_count = 18
summary_line = str(interview_count) + " interviews analyzed"
print("#5 summary_line:", summary_line)

# 6. evaluate: one number is equal to or greater than another
meets_min_sample = interview_count >= 15
print("#6 meets_min_sample (>= 15):", meets_min_sample)

# 7. evaluate: two numbers are not equal
planned_focus_groups = 4
actual_focus_groups = 3
focus_group_gap = planned_focus_groups != actual_focus_groups
print("#7 focus_group_gap (planned != actual):", focus_group_gap)

# 8. evaluate: two previously assigned variables are equal
same_number = total_sites == interview_count
print("#8 total_sites == interview_count:", same_number)

# 9. evaluate: int equals same number as a string?
int_vs_str_equal = 10 == "10"  # False (different types)
print("#9 10 == '10':", int_vs_str_equal)

# 10. evaluate: int equals same number as a float?
int_vs_float_equal = 10 == 10.0  # True (values equal)
print("#10 10 == 10.0:", int_vs_float_equal)

# 11. evaluate: the string "None" equals the None data type?
string_none_vs_None = "None" == None  # False
print("#11 'None' == None:", string_none_vs_None)

# 12. assign an array (list) to a variable (codes from an excerpt)
codes = ["access", "ancestry", "health", "mutual aid"]
print("#12 codes:", codes)

# 13. append a value to the list 
codes.append("seasonality")
print("#13 codes after append:", codes)

# 14. assign a value from the array by indexing
first_code = codes[0]  # "access"
print("#14 first_code:", first_code)

# 15. assign a substring of the variable from (4)
# remove the prefix "Qualitative Memo: " to leave just the title
trimmed_title = report_title[len("Qualitative Memo: "):]
print("#15 trimmed_title:", trimmed_title)

# 16. assign nested lists (mini table): [site_name, weekly_customers, accepts_EBT]
markets = [
    ["West Side Market", 850, True],
    ["Southtown Pop-up", 220, False],
    ["Lakeview Thursday", 430, True],
]
print("#16 markets[0]:", markets[0])
print("     name:", markets[0][0], "| customers:", markets[0][1], "| EBT:", markets[0][2])
