# Write a function that prints "Hello_USERNAME"
def hello_name(user_name):
    print("Hello_" + user_name.upper())

def hello_name(user_name):
    print('hello_' + user_name)


hello_name('Chris')


def first_odds():
    odd_number = list(range(1, 100, 2))
    print(odd_number)

# Write a function to return the max number in a list
a_list = range(1, 200)

def max_num_in_list(a_list):
    print(max(a_list))


max_num_in_list(a_list)


# Write a function to determine if any given year is a leap year

def is_leap_year(a_year):
    a_year = 2022
    if (a_year % 400 == 0) or (a_year % 4 == 0 and a_year % 100 != 0):
        print(True)
        print(str(a_year) + " is a leapyear")
    else:
        print(False)
        print(str(a_year) + " is not a leapyear")


is_leap_year(a_year)

# Write a function to check if all numbers in a list are consecutive


def is_consecutive(a_list):
    """checks if numbers in a list are consecutive"""
    while len(a_list[:]) >= 2:        
        if a_list.pop() == a_list[-1] + 1:
            continue
        else:
            return False
    return True

print(is_consecutive([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 16]))
