def days_in_month(month, year):
    if month == 2:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return 29 
        else:
            return 28  
    elif month in [4, 6, 9, 11]:
        return 30  
    else:
        return 31 
month = int(input("Enter month (1-12): "))
year = int(input("Enter year: "))

if 1 <= month <= 12:
    days = days_in_month(month, year)
    print(f"The month {month} of year {year} has {days} days.")
else:
    print("Invalid month. Please enter a number between 1 and 12.")
