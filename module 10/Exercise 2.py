class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def floor_up(self):
        self.current_floor += 1
        print(f"Floor: {self.current_floor}")

    def floor_down(self):
        self.current_floor -= 1
        print(f"Floor: {self.current_floor}")

    def go_to_floor(self, floor):
        if floor > self.current_floor:
            while self.current_floor < floor:
                self.floor_up()
        elif floor < self.current_floor:
            while self.current_floor > floor:
                self.floor_down()


class Building:
    def __init__(self, bottom_floor, top_floor, elevator):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = []

        for i in range(elevator):
            self.elevators.append(Elevator(bottom_floor, top_floor))

    def run_elevator(self, elevator, destination_floor):
        self.elevators[elevator].go_to_floor(destination_floor)