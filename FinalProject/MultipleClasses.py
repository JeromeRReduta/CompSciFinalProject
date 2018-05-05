# Take any class
class Class():
    def __init__(self, number):
        self.name = "Johnathan"
        self.number = str(number)

    def sayname(self):
        print("This is " + self.name + " #" + self.number)

# i = 1
# # All that matters is that there are as many items in "numbers" as classes you want to make
# numbers = [0, 1, 2, 3, 4]
# classes = []
#
# for number in numbers:
#     #reassigns items in list as classes
#     numbers[number] = Class(i)
#     classes.append(numbers[number])
#     i += 1
#
# # Lists all classes' names, to make sure it works
# for thing in classes:
#     thing.sayname()

# Scalable up to maybe 30 (you have to type the numbers in the list yourself, to save on calculations)
# className = Class you want to make an instance of (e.g. Class())
# howMany = How many instances you want to make

# Scalable pu to maybe 30 (you have to type in the numbers in listofClasses yourself, to save on calc)
# className = name of class you want to make instance of, WIHTOUT parentheses
# i = index, made specificaly for test function. You can remove it

#
# def createClasses(className, i):
#     global listofClasses
#     listofClasses = [0, 1, 2, 3, 4, 5, 6]
#
#     for item in listofClasses:
#         #reassigns items in list as classes
#         listofClasses[item] = className(i)
#         i+=1
#
#
# # Calling function, Making every function say name
# createClasses(Class, 0)
#
# for item in listofClasses:
#     item.sayname()
#
# # Function, infinitely scalable (until hardware breaks)
# # howMany = how many instances you want to make
# def createManyClasses(className, howMany, i):
#     global listOfManyClasses
#     listOfManyClasses = []
#     index = 0
#     while index < howMany:
#         listOfManyClasses.append(index)
#         index += 1
#     for item in listOfManyClasses:
#         listOfManyClasses[item] = className(i)
#         i += 1
#
# createManyClasses(Class, 5, 0)
# for things in listOfManyClasses:
#     things.sayname()

list = []
i = 0
for item in [0, 1, 2, 3, 4, 5]:
    item = Class(i)
    list.append(item)
    i+=1

for thing in list:
    thing.sayname()