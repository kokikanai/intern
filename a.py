def is_leap_year(year):
    return year % 4 == 0 and year % 100 != 0 or year

print is_leap_year(2000)
print is_leap_year(2001)
print is_leap_year(2004)
print is_leap_year(2100)