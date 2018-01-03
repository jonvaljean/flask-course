def methodception(another):
    return another()

def add_two_numbers():
    return 35+77

print(methodception(add_two_numbers))  #pass method as parameter

# lamda

print(methodception(lambda: 35+77)) # lamdaalsways in one line

# style of programming called declarative or functional programming

my_list = [13,16,77,484]

# to remove all elements that are even

print(list(filter(lambda x: x != 13, my_list)))  #takes a function and iterable
