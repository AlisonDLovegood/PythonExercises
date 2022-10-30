number = int(input("How many numbers do you will use? "))
list = []

for i in range(number):
    n = int(input("Enter with a number: "))
    list.append(n)

print("Sum of them:", sum(list))
