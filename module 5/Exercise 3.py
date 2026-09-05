smallest = None
largest = None

while True:
    number = input("Enter a number (or press Enter to quit): ")

    if number == "":
        break

    number = float(number)

    if smallest is None:
        smallest = number
        largest = number
    else:
        if number < smallest:
            smallest = number

        if number > largest:
            largest = number

print("Smallest number:", smallest)
print("Largest number:", largest)




    




    