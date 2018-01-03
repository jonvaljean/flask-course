lottery_player_dict =    {
    'name':'Rolf',
    'numbers': (5,9,12,3,1,21)
}

class LotteryPlayer:
    def __init__(self,name):
        self.name = name
        self.numbers = (5,9,12,3,1,21)

    def total(self):
        return sum(self.numbers)

player_one = LotteryPlayer("Rolf")
player_two = LotteryPlayer("John")

#print(player_one.name)
#print(player_two.name)

class Student:
    def __init__(self,name,school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

    def go_to_school(self):
        print("I'm going to {}".format(self.school))

    @staticmethod
    def go_to_scool_static():
        print("I'm going to static school")

    @classmethod
    def go_to_school_class(cls):
        print("I'm a {}".format(cls))

anna = Student("Anna","MIT")
anna.marks.append(56)
anna.marks.append(71)
print(anna.marks)
print(anna.average())

anna.go_to_school()
anna.go_to_scool_static()
Student.go_to_school_class()
