from movement import *
from snapshot import *

import sys

class Drone:
    def __init__(self):
        self.command = []
        self.movement = Movement()
        self.snapshot = Snapshot()

    def read_commands(self, file_name):     
        instructor_file = open(file_name, "r")
        line = instructor_file.readlines()
        self.command = line[0]
        instructor_file.close()
     
    def process(self):        
        for instructor in self.command:
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

    def get_billboard_num(self):
        return self.snapshot.unique_billboard_number()


def main(argv):
    drone = Drone()
    drone.read_commands(argv)
    drone.process()
    billboard_num = drone.get_billboard_num()
    print("The number of billboards that are captured at least once is " +
          str(billboard_num))


if __name__ == "__main__":
    main(sys.argv[1])
