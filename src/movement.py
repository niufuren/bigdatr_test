class Movement:
    def __init__(self):
        self.x = 0
        self.y = 0

    def move_down(self):
        self.y = self.y - 1

    def move_up(self):
        self.y = self.y + 1

    def move_right(self):
        self.x = self.x + 1

    def move_left(self):
        self.x = self.x - 1
