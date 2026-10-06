# match-case statements (switch-case statements) = an alternative to writing long chains of if-elif-else statements.
#                               execute some code if a value matches a 'case'
#                               Benefits: cleaner and syntax is more readable

    # 1. The Problem with Long if-elif-else Chains:
def day_of_week(day):
    if day == 1:
        return "It is Sunday"
    elif day == 2:
        return "It is Monday"
    elif day == 3:
        return "It is Tuesday"
    elif day == 4:
        return "It is Wednesday"
    elif day == 5:
        return "It is Thursday"
    elif day == 6:
        return "It is Friday"
    elif day == 7:
        return "It is Saturday"
    else:
        return "Not a valid day"

print(day_of_week(1))
print(day_of_week(2))
print(day_of_week(7))




print()
                # instead of repeating 'elif day ==....' seven-times, we use -> match-case:

    # 2. The Solution Using match and case:
def day_of_week(day):
    match day:
        case 1:
            return "It is Sunday"
        case 2:
            return "It is Monday"
        case 3:
            return "It is Tuesday"
        case 4:
            return "It is Wednesday"
        case 5:
            return "It is Thursday"
        case 6:
            return "It is friday"
        case 7:
            return "It is Saturday"
        case _:
            return "Not a Valid day"


print(day_of_week(1))   # Sunday
print(day_of_week(5))   # Thursday
print(day_of_week(15))  # Not a valid day
print(day_of_week("dosa")) # Not a valid day


print()

# code working/explanation:
'''
1. match day: Tells Python: "Inspect the value inside 'day'."
2. case 1: Checks if day == 1. If yes, it runs that block and immediately finishes.
3. ** case _: (Wildcard): The underscore _ acts as the default / catch-all case (identical to 'else:').
                             If none of the numbers from 1-7 match, this block runs automatically.
        case _:   =    else:
        case(space)_     -->>  space is important
'''
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# 3. Combining Multiple Cases Using the Pipe (|) Operator
#       What if multiple cases share the exact same outcome? Instead of writing duplicate code, combine them using the vertical bar | (which means OR).



def is_weekend(day):
    match day:
        case "Saturday" | "Sunday":
            return True
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return False
        case _:
            return False

print(is_weekend("Sunday"))     # True
print(is_weekend("Monday"))     # False
print(is_weekend("pizza"))      # False

# here, write 'case' alone, not as case 1, case 2.
# at last, case(space)_:    -->> case _: --> (wildcard) ---> else:




# visualize:
'''
day = "Sunday"

match day:
   ├── case "Saturday" | "Sunday"  ──► Match! ──► return 'True'
   ├── case "Monday" | ...
   └── case _
'''