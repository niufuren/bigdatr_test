from movement import *
from snapshot import *
from functools import partial

import sys


class Drone:
    def __init__(self):
        self.movement = Movement()
        self.snapshot = Snapshot()

    def process(self, instructor):
        if instructor == "^":
            self.movement.move_up()
        elif instructor == "v":
            self.movement.move_down()
        elif instructor == "<":
            self.movement.move_left()
        elif instructor == ">":
            self.movement.move_right()
        elif instructor == "x":
            self.snapshot.billboard_shot(self.movement)
        else:
            print ("cann't recognise the instructor: " + instructor)

    def read_process_commands(self, file_name):
        with open(file_name) as file:
            for instructor in iter(partial(file.read, 1), ''):
                self.process(instructor)

    def get_billboard_num(self):
        return self.snapshot.unique_billboard_number()

    def get_coordinate(self):
        x_coordinate = self.movement.x
        y_coordiante = self.movement.y

        coordiante = (x_coordinate, y_coordiante)

        return coordiante


def main(argv):
    drone = Drone()
    drone.read_process_commands(argv)
    # drone.process()
    billboard_num = drone.get_billboard_num()
    print("The number of billboards that are captured at least once is " +
          str(billboard_num))

    drone_position = drone.get_coordinate()
    print("The coordinate of the final location of the drone is " +
          str(drone_position))


if __name__ == "__main__":
    main(sys.argv[1])
