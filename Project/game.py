from player import Player
from room import Room
from item import Item
import os


def read_file(filename):
    #Read text from a file in the project folder.
    file_path = os.path.join(os.path.dirname(__file__), filename)

    with open(file_path, "r") as file:
        return file.read()


def start_game(player):
    # Display the introduction and instructions.
    print(read_file("intro.txt"))
    print(read_file("instructions.txt"))

    player.started = True


def find_item(player):
    #Let the player collect an item from the current room.
    player.collect_item()


def check_inventory(player):
    #Display all items collected by the player.
    print("\nYOUR INVENTORY")

    if len(player.items) == 0:
        print("Your inventory is empty.")
    else:
        for item in player.items:
            print(item.name, "-", item.weight, "kg")


def view_progress(player):
   #Display the player's current progress.
    print("\nYOUR PROGRESS")
    print("Current location:", player.location.name)
    print("Points:", player.points)
    print("Items collected:", len(player.items))

    if player.started:
        print("Game started: Yes")
    else:
        print("Game started: No")


def move_player(player, rooms):
    #Allow the player to move to another room.
    print("\nLOCATIONS")

    for number, room in enumerate(rooms, 1):
        print(number, "-", room.name)

    choice = input("Choose a location: ")

    if choice.isdigit():
        choice = int(choice)

        if 1 <= choice <= len(rooms):
            player.move(rooms[choice - 1])
            print("You moved to:", player.location.name)
        else:
            print("Invalid room number.")
    else:
        print("Please enter a number.")


def solve_puzzle(player):
    #Give the player a puzzle based on their current location.
    if player.location.name == "Forest":
        if "Forest" in player.solved_puzzles:
            print("You have already solved the Forest puzzle.")
            return 0

        print("\nFOREST PUZZLE")
        print("A sign says:")
        print("I have 3 sides. What shape am I?")

        answer = input("Your answer: ").lower()

        if answer == "triangle":
            print("Correct! You earned 1 point.")
            player.points += 1
            player.solved_puzzles.append("Forest")
            return 1

        print("That answer is incorrect.")
        return 0

    if player.location.name == "Hill":
        if "Hill" in player.solved_puzzles:
            print("You have already solved the Hill puzzle.")
            return 0

        print("\nHILL PUZZLE")
        print("What is 5 + 5?")

        answer = input("Your answer: ")

        if answer == "10":
            print("Correct! You earned 1 point.")
            player.points += 1
            player.solved_puzzles.append("Hill")
            return 1

        print("That answer is incorrect.")
        return 0

    if player.location.name == "River":
        if "River" in player.solved_puzzles:
            print("You have already solved the River puzzle.")
            return 0

        print("\nRIVER PUZZLE")
        print("Which of these is safest to drink?")
        print("1. Polluted water")
        print("2. Clean drinking water")

        answer = input("Choose 1 or 2: ")

        if answer == "2":
            print("Correct! You earned 1 point.")
            player.points += 1
            player.solved_puzzles.append("River")
            return 1

        print("That answer is incorrect.")
        return 0

    print("There is no puzzle in this location.")
    return 0


def check_ending(player):
    #Check whether the player has completed the game.
    if player.points >= 3 and len(player.items) >= 3:
        print("\n================================")
        print("CONGRATULATIONS!")
        print("================================")
        print("You solved the mystery of the water supply.")
        print("The town's water problem has been fixed!")
        print("You completed UNRAVEL!")
        print("================================")

        return True

    return False


def save_game(player):
    #Save the player's current game state.
    file_path = os.path.join(os.path.dirname(__file__), "save.txt")

    with open(file_path, "w") as file:
        file.write(player.name + "\n")
        file.write(player.location.name + "\n")
        file.write(str(player.points) + "\n")

        for item in player.items:
            file.write("ITEM:" + item.name + "\n")

        for puzzle in player.solved_puzzles:
            file.write("PUZZLE:" + puzzle + "\n")

    print("Game saved successfully!")


def load_game(rooms, items):
    #Load a previously saved game.
    file_path = os.path.join(os.path.dirname(__file__), "save.txt")

    try:
        with open(file_path, "r") as file:
            lines = file.readlines()

        name = lines[0].strip()
        location_name = lines[1].strip()
        points = int(lines[2].strip())

        location = None

        for room in rooms:
            if room.name == location_name:
                location = room
                break

        if location is None:
            print("Saved location could not be found.")
            return None

        player = Player(name, location)
        player.points = points

        for line in lines[3:]:
            line = line.strip()

            if line.startswith("ITEM:"):
                item_name = line[5:]

                for item in items:
                    if item.name == item_name:
                        player.items.append(item)

            elif line.startswith("PUZZLE:"):
                puzzle_name = line[7:]
                player.solved_puzzles.append(puzzle_name)

        player.started = True

        print("Saved game loaded!")
        return player

    except FileNotFoundError:
        print("No saved game found.")
        return None


def create_new_player(town):
    """Ask for the player's name and age and create a player."""
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))

    if age < 12:
        print("You are a minor. The game is shutting down.")
        return None

    return Player(name, town)


def main():

    # Create items.
    emerald = Item("emerald", 0.1)
    diamond = Item("diamond", 0.5)
    ruby = Item("ruby", 0.02)
    sapphire = Item("sapphire", 0.25)

    items = [emerald, diamond, ruby, sapphire]

    # Create rooms.
    town = Room("Town Square", None)
    forest = Room("Forest", emerald)
    hill = Room("Hill", diamond)
    river = Room("River", ruby)
    cave = Room("Cave", sapphire)

    rooms = [town, forest, hill, river, cave]

    print("\n=== UNRAVEL ===")
    print("1. New Game")
    print("2. Continue Game")

    choice = input("Choose an option: ")

    if choice == "2":
        player = load_game(rooms, items)

        if player is None:
            print("Starting a new game.")
            player = create_new_player(town)
    else:
        player = create_new_player(town)

    if player is None:
        return

    print("\nHello, " + player.name + "!")
    print("Welcome to Unravel.")

    while True:

        print("\n=== MAIN MENU ===")
        print("1. Start Game")
        print("2. Move to another location")
        print("3. Find an item")
        print("4. Solve puzzle")
        print("5. Check inventory")
        print("6. View progress")
        print("7. Save Game")
        print("8. Quit")

        command = input("Select your choice: ")

        if command == "1":
            start_game(player)

        elif command == "2":
            move_player(player, rooms)

        elif command == "3":
            find_item(player)

        elif command == "4":
            solve_puzzle(player)

            if check_ending(player):
                break

        elif command == "5":
            check_inventory(player)

        elif command == "6":
            view_progress(player)

        elif command == "7":
            save_game(player)

        elif command == "8" or command.lower() == "lopeta":
            print("Exiting the game. Goodbye!")
            break

        else:
            print("Invalid choice.")

        if check_ending(player):
            break


if __name__ == "__main__":
    main()

       