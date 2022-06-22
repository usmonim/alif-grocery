import re
import sys

class ActionOne:
    def __init__(self, name, addition): #constructor
        # self.data_array = data_array
        self.name = name
        self.addition = addition

    def adding(self):
        f = open(self.name, 'a+')
        f.seek(0)
        # If file is not empty then append '\n'
        data5 = f.read(100)
        if len(data5) > 0:
            f.write("\n")
        # Append text at the end of file
        f.write(self.addition)
        f.close()


#A list which will store the data from file
data = []

#Getting filename and the action number from command line arguments
file_name = sys.argv[1]
action = sys.argv[2];

with open(file_name, 'r+') as file:
    data = [line.strip() for line in file] #take all data from opened file

#if user enter 1 in command line argument then we perform action "Добавить в список/Add to list"
if int(action) == 1:
#Ask user to enter what he want yo add to the list
    add = input("1 Добавить в список: ")
    execute = ActionOne(file_name, add)
    execute.adding()
    # print(data)
    # data.append(add)