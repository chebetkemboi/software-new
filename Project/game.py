
from player import Player
from room import Room
from item import Item


def start_game():
    print("Starting the game...")


def find_item(player):
    player.collect_item()


def check_inventory(player):
    print("Your inventory:")

    if len(player.items) == 0:
        print("Your inventory is empty.")
    else:
        for item in player.items:
            print(item.name, "-", item.weight, "kg")


def view_progress(player):
    print("Viewing progress...")
    print("Current location:", player.location.name)
    print("Items collected:", len(player.items))


def move_player(player, rooms):
    print("\nChoose a room:")

    for number, room in enumerate(rooms, start=1):
        print(number, "-", room.name)

    choice = input("Select a room: ")

    if choice.isdigit():
        choice = int(choice)

        if 1 <= choice <= len(rooms):
            destination = rooms[choice - 1]
            player.move(destination)
        else:
            print("Invalid room number.")
    else:
        print("Please enter a number.")


def main():
    Name = input("Enter Name:")
    Age = float(input("Enter Age:"))

    print(Name)
    print(Age)

    if Age < 12:
        print("You are a minor. The game is shutting down.")
        return

    else:
        print("Hello," + Name + "!")
        print("Welcome to Unravel")

        key = Item("Key", 0.1)
        book = Item("Book", 0.5)
        coin = Item("Coin", 0.02)

        library = Room("Library", key)
        hallway = Room("Hallway", book)
        garden = Room("Garden", coin)

        rooms = [library, hallway, garden]

        player = Player(Name, library)

        while True:
            print()
            print("=== MAIN MENU ===")
            print("1. Start Game")
            print("2. Move to another room")
            print("3. Find an item")
            print("4. Check inventory")
            print("5. View progress")
            print("6. Lopeta")

            command = input("Select your choice (1-6): ")

            if command == "1":
                start_game()

            elif command == "2":
                move_player(player, rooms)

            elif command == "3":
                find_item(player)

            elif command == "4":
                check_inventory(player)

            elif command == "5":
                view_progress(player)

            elif command == "6" or command.lower() == "lopeta":
                print("Exiting the game. Goodbye!")
                break

            else:
                print("Invalid choice. Please select a valid option (1-6).")


if __name__ == "__main__":
    main()
    




   
   
       