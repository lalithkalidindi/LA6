#-------------------------------------------------------------------------------
# LA6.py
# Name: LK Kalidindo
# Python Version: 2.XX or 3.XX
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines as set forth by the
# instructor and the class syllabus.
#-------------------------------------------------------------------------------
# References:
#-------------------------------------------------------------------------------
# Comments to grader:
#-------------------------------------------------------------------------------
# Code: Code starts here
#-------------------------------------------------------------------------------

class SpecialDict(dict):
    def setdefault(self, key, value):
        # your code here
        # check the conditions on the key
        # if conditions are not met
        # return informational message - see sample I/O
        # else call super class's setdefault method
        # .setdefault takes key and value as parameter
        # return informational message - see sample I/O

        # making an if statment of the length of the key
        if len(key) != 5:
            # making a return statment
            return "ID length must be 5 characters"

        # checking if the ID starts with G
        if key[0] != "G":
            return "ID must start with G"

        # putting the students in the dictionary
        super().setdefault(key, value)  # dictionary has key value

        # returns the student added
        return "Student added!"


# creating a class called department
class Department(object):

    roster = SpecialDict()

    # making a function for adding the student
    def add_student(self):
        # making a string for the student to enter their ID
        gmu_id = input("Enter your G Number: ")

        # having the user to enter the full name
        full_name = input("Please enter the full name: ")

        # format of the message
        message = Department.roster.setdefault(gmu_id, full_name)
        print(message)

    # making a function of print roster
    def print_roster(self):
        # making a for loop of id, full name in the department for roster
        for gmu_id, full_name in Department.roster.items():
            print(f"{gmu_id}->{full_name}")  # format which is id and full name


# the choice is an empty set
choice = ''

# making a while loop which not equals to n
while choice != 'n':
    dept = Department()  # dept which stands for department
    dept.add_student()  # the department is adding student
    choice = input("Continue adding? (y/n): ")  # it is asking if the user wants to continue

print("Student Roster")  # printing the student roster
dept.print_roster()
