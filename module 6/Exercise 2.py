numbers = []

while True:
    value = input("Enter a number: ")

    if value == "":
        break

    numbers.append(float(value))

numbers.sort(reverse=True)

print("The greatest numbers in descending order:")

for number in numbers[:5]:
    print(number)
    