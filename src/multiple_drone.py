import drone
import sys

TOTAL_DRONE_NUMBER = 2


class MultipleDrone(drone.Drone):
    def read_commands(self, file_name, total_drone_number, order):
        '''
        read the command from a txt file, and get the paticular commands
        for the drone with the order number among multiple drones.
        '''
        drone.Drone.read_commands(self, file_name)
        command_all = self.command
        self.command = []

        # get the total length of the commands
        command_all_length = len(command_all)

        command_length = command_all_length / total_drone_number

        if order <= command_all_length % total_drone_number:
            command_length = command_length + 1

        # get the commands for the drone with the order number
        for i in range(0, command_length):
            ind_command_all = order + i * total_drone_number - 1

            self.command.append(command_all[ind_command_all])

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
    drone_first = MultipleDrone()
    drone_first.read_commands(argv, TOTAL_DRONE_NUMBER, 1)
    drone_first.process()

    drone_second = MultipleDrone()
    drone_second.read_commands(argv, TOTAL_DRONE_NUMBER, 2)
    drone_second.process()

    billboard_num = drone_first.billboard_number_union(drone_second)

    print("The number of billboards that are captured at least once is " +
          str(billboard_num))


if __name__ == "__main__":
    main(sys.argv[1])
