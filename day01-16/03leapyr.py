""" Checking if a year is a leap year"""

for year in range(1900, 2101, 4):
    leap100 = year % 100
    leap400 = year % 400
    leap004 = year % 4

    if leap004 == 0:
        if leap100 == 0:
            if leap400 == 0:
                print(f"leap year {year}")
            else:
                print(f'not leap {year}')
        else:
            print(f'leap year {year}')
    else:
        print(f'not leap {year}')
    
    
    

