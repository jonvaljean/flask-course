# should_continue = True
#if should_continue:
    #print("hello")

# known_people = ["John","Anna", "Mary"]
# person = input ("Enter the person you know: ")
#
# if person in known_people:
#     print("You know {} !".format(person))
#
# else:
#     print("You don't know {} !".format(person))

def who_do_you_know():
    #ask user for list of people they known_people
    #split the string into a list
    #return that list
    input_people = input("type list of people you know, comma separated: ")
    people = input_people.split(",")

    people_without_spaces = [people_lower.lower for people_lower in people]

    return people_without_spaces

def ask_user(list):
    #ask user for their name
    #see if their name is in the list of people they know
    #print out that they know the person
    input_name = input("Give me a name, please ")
    if input_name in list:
        print("Yes you know {}".format(input_name))

list = who_do_you_know()

print(list)

ask_user(list)
