# Note: Apply to Bunny classes - make many bunny classes - if bunny "withdraws" remove that specific class from list
class Class():
    def __init__(self, number):
        self.name = "Johnathan"
        self.number = str(number)

    def sayname(self):
        print("This is " + self.name + " #" + self.number)

i = 1
# Does not matter what items are in here, just that there are as many items in list as classes you want to make
numbers = [0, 1, 2, 3, 4]
classes = []
for number in numbers:
    #reassigns items in list as classes
    numbers[number] = Class(i)
    classes.append(numbers[number])
    i += 1


for thing in classes:
    thing.sayname()