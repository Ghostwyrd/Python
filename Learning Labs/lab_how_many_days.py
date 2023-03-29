def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

    
def days_in_month(year, month):
    mo_30 = [4, 6, 9, 11]
    if month == 2 and is_year_leap(year):
        res = 29
    elif month == 2 and not is_year_leap(year):
        res = 28
    elif (month in mo_30):
        res = 30
    else:
        res = 31
    print(res)
    return res


test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]

for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo,  "->", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
          print("OK")
    else:
        print("Failed")
