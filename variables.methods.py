a = 5
b = 10
my_variable = 56
any_variable_name = 19

string_variable = "hello"
single_quotes = 'srings can have single quotes'

#print(my_variable)
#print(string_variable)

##

def my_print_method(my_argument):
    print(my_argument)

my_print_method("floo floo")

def my_multiply_method(num1,num2):
    return num1 * num2

result = my_multiply_method(5,3)
print(result)
my_print_method(result)

my_print_method(my_multiply_method(5,3))
