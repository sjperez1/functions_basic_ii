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
def print_and_return(numberlist):
    print(numberlist[0])
    return numberlist[1]
print(print_and_return(two_numbers))

# 3. First Plus Length
first_plus_length_list = [4,2,8,9,3,7,5]
def first_plus_length(firstlengthlist):
    return firstlengthlist[0] + len(firstlengthlist)
print(first_plus_length(first_plus_length_list))

# 4. Values Greater than Second
original_list = [7,3,4,8,1,6,2]
new_list = []
def values_greater_than_second(greaterthansecondlist):
    if len(greaterthansecondlist) < 2:
        return False
    else:
        for i in range(0,len(greaterthansecondlist)-1):
            if greaterthansecondlist[i] > greaterthansecondlist[1]:
                new_list.append(greaterthansecondlist[i])
    print(len(new_list))
    return new_list
print(values_greater_than_second(original_list))

# 5. This Length, That Value
lengthvaluelist = [ ] 
def length_and_value(size,value):
    for i in range(0, size):
        lengthvaluelist.append(value)
    return lengthvaluelist
print(length_and_value(5,8))