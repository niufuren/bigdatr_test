class Snapshot:
    def __init__(self):
        self.position = []
        self.snapshot_num = []

    def billboard_shot(self, movement):
        billboard_coordinate = (movement.x, movement.y)
        ''' if the coordinate is in the position list '''
        if billboard_coordinate in self.position:
            billboard_index = self.position.index(billboard_coordinate)
            self.snapshot_num[billboard_index] = \
                self.snapshot_num[billboard_index] + 1
        else:
            ''' if the coordinate is not in the position list
                insert the coordinate of the billboard to the list of position
            '''
            self.position.append(billboard_coordinate)
            self.snapshot_num.append(1)

    def unique_billboard_number(self):

        billboard_num = len(self.position)
        return billboard_num
