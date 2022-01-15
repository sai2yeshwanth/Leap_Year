# find the given year is Leap Year or Not
#  1. If year is divisible by 4, 100, 400 is a leap year.
# 2. If year is divisible by 4 and Not divisible by 100 is also a leap year.
# 3. If year is divisible by 4 and 100 is Not a leap year.

def leap_year(year):
    # checking the given year is leap year or not
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                print(f"The '{year}' is a Leap Year")
            else:
                print(f"The '{year} is Not a Leap Year'")
        else:
            print(f"The '{year}' is a Leap Year.")

    else:
        print(f"The '{year}' is Not a Leap Year. ")



    return 

year = int(input("Enter the Year to check if it's a Leap Year or Not : "))
# calling leap_year function
leap_year(year)
