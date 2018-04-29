# Note: Apply to Bunny classes - make many bunny classes - if bunny "withdraws" remove that specific class from list
class Class():
    def __init__(self, number):
        self.name = "Johnathan"
        self.number = str(number)

    def sayname(self):
        print("This is " + self.name + " #" + self.number)

i = 1
alphabet = ["a", "b", "c", "d", "e"]
classes = []
numbers = [0, 1, 2, 3, 4]
for number in numbers:

    alphabet[number] = Class(i)
    classes.append(alphabet[number])
    i += 1

for thing in classes:
    thing.sayname()