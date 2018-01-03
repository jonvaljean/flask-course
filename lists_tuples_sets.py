my_variable = "hello"

grades = [77,80,90] #lists are most flexible, mutable

tuple_grades = (77,80,90)  #tuples are immutable

set_grades = {77,89,90} #unique and unordered, mutable


#print(grades)
#print(sum(grades)/len(grades))

#print(set_grades)


#print(tuple_grades[0])

your_lottery_numbers = {1,2,3,4,5}
winning_lottery_numbers = {1,3,5,7,8,11}

#print(your_lottery_numbers.union(winning_lottery_numbers))
set_result = your_lottery_numbers.difference(winning_lottery_numbers)

#print(set_result)

my_tuple = 5,4,7
print(my_tuple)
