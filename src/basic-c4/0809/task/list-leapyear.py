leap = []

for leap_year in range(2000, 2101):
    if ((leap_year % 4 == 0) or (leap_year % 100 != 0)) and (leap_year % 4 == 0):
        leap.append(leap_year)

    else:
        pass
print(leap)
