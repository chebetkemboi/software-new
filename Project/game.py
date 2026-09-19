Name = input("Enter Name:")
Age = float(input("Enter Age:"))

print(Name)
print(Age)

if Age < 12:
    print("You are a minor.The game is shutting down.")
else:
    print("Hello," + Name + "!")
    print("Welcome to Unravel")

    inventory = []

    def start_game():
        print("Starting the game...")

    def find_item():
        item = input("What item did you find? ")
        inventory.append(item)
        print(item, "has been added to your inventory.")

    def check_inventory():
        print("Your inventory:")

        for item in inventory:
            print(item)

    def view_progress():
        print("Viewing progress...")


    while True:
        print()
        print("=== MAIN MENU ===")
        print("1. Start Game")
        print("2. Find an item")
        print("3. Check inventory")
        print("4. View progress")
        print("5. Lopeta")

        command = input("Select your choice (1-5): ")

        if command == "1":
            start_game()

        elif command == "2":
            find_item()

        elif command == "3":
            check_inventory()

        elif command == "4":
            view_progress()

        elif command == "5":
            print("Exiting the game. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option (1-5).")





   
   
       