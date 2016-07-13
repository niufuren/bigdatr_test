import drone
from functools import partial
import sys

TOTAL_DRONE_NUMBER = 2


class MultipleDrone(drone.Drone):
    def __init__(self, total_drone_number, order):
        drone.Drone.__init__(self)
        self.total_drone_number = total_drone_number
        self.order = order

    def read_process_commands(self, file_name):
        '''
        read the command from a txt file, and get the paticular commands
        for the drone with the order number among multiple drones.
        '''
        with open(file_name) as file:
            instructor_count = 1
            for instructor in iter(partial(file.read, 1), ''):
                if instructor_count <= self.total_drone_number:
                    if instructor_count == self.order:
                        drone.Drone.process(self, instructor)
                else:
                    if self.order != self.total_drone_number:
                        if (instructor_count % self.total_drone_number ==
                                self.order):
                            drone.Drone.process(self, instructor)
                    else:
                        if instructor_count % self.total_drone_number == 0:
                            drone.Drone.process(self, instructor)

                instructor_count = instructor_count + 1

    def billboard_number_union(self, another_drone):
        '''get the number of unique billboards that are snapshotted
        by itself and another drone.
        '''
        billboard_set1 = set(self.snapshot.position)
        billboard_set2 = set(another_drone.snapshot.position)

        set_unique = billboard_set1.union(billboard_set2)
        set_num = len(set_unique)

        return set_num

def main(argv):
    drone_first = MultipleDrone(TOTAL_DRONE_NUMBER, 1)
    drone_first.read_process_commands(argv)

    drone_second = MultipleDrone(TOTAL_DRONE_NUMBER, 2)
    drone_second.read_process_commands(argv)

    billboard_num = drone_first.billboard_number_union(drone_second)

    print("The number of billboards that are captured by " +
          "two drones at least once is " + str(billboard_num)
          )

    drone_first_position = drone_first.get_coordinate()
    print("The coordinate of the final location of the first drone is " +
          str(drone_first_position))

    drone_second_position = drone_second.get_coordinate()
    print("The coordinate of the final location of the second drone is " +
          str(drone_second_position))


if __name__ == "__main__":
    main(sys.argv[1])
