class Player:

    def __init__(self, name, location):
        self.name = name
        self.items = []
        self.location = location
        self.points = 0
        self.solved_puzzles = []
        self.started = False

    def move(self, destination):
        self.location = destination
        print("You moved to", destination.name)

    def collect_item(self):
        if self.location.item is not None:
            item = self.location.item
            