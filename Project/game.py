Name = input("Enter Name:")
Age = float(input("Enter Age:"))

print(Name)
print(Age)

if Age < 12:
    print("You are a minor.The game is shutting down.")
else:
    print("Hello," + Name + "!")
    print("Welcome to Unravel")

while True:
    print()
    print("=== MAIN MENU ===")
    print("1. Start Game")
    print("2. Check inventory")
    print("3. View proggrees")
    print("4. Lopeta")

    command = input("Select your choice (1-4): ")

    if command == "1":
       print("Starting the game...") 
    elif command == "2":
       print("Checking inventory...")  
    elif command == "3":
       print("Viewing progress...") 
    elif command == "4":
       print("Exiting the game. Goodbye!")
       break
    else:
       print("Invalid choice. Please select a valid option (1-4).")
       