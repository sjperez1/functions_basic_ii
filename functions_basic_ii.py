# 1. Countdown
# Do not put countdown_list in for loop.
countdown_list = []
def countdown(num):
    for i in range(num, -1, -1):
        countdown_list.append(i)
    return countdown_list
print(countdown(6))

# 2. Print and Return
two_numbers = [6, 4]
def print_and_return(number_list):
    print(number_list[0])
    return number_list[1]
print(print_and_return(two_numbers))

# 3. First Plus Length
first_plus_length_list = [4,2,8,9,3,7,5]
def first_plus_length(first_length_list):
    return first_length_list[0] + len(first_length_list)
print(first_plus_length(first_plus_length_list))

# 4. Values Greater than Second
original_list = [7,3,4,8,1,6,2]
new_list = []
def values_greater_than_second(greater_than_second_list):
    if len(greater_than_second_list) < 2:
        return False
    else:
        for i in range(0,len(greater_than_second_list)-1):
            if greater_than_second_list[i] > greater_than_second_list[1]:
                new_list.append(greater_than_second_list[i])
    print(len(new_list))
    return new_list
print(values_greater_than_second(original_list))

# 5. This Length, That Value
length_value_list = [ ] 
def length_and_value(size,value):
    for i in range(0, size):
        length_value_list.append(value)
    return length_value_list
print(length_and_value(5,8))