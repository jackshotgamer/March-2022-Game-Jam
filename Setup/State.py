import arcade
from Setup import vector


class State:
    def __init__(self):
        self.player_pos = vector.Vector(0, 0)
        self.total_player_size = vector.Vector(33, 50)
        self.player_head_size = vector.Vector(33, 23)
        self.player_body_size = vector.Vector(18, 27)
        self.window = None
        self.velocity = vector.Vector(0, 0)

    @property
    def screen_center(self):
        return vector.Vector(self.window.width / 2, self.window.height / 2)

    def update_player_pos(self, x, y):
        self.player_pos = vector.Vector(x, y)

    def move(self, velocity, sprinting=False):
        if sprinting:
            self.velocity = velocity * 2
        else:
            self.velocity = velocity

    def move_player(self, time_delta):
        movement = self.velocity * time_delta
        if self.player_pos.x + movement.x > (self.total_player_size.x / 2) and self.player_pos.y + movement.y > (self.total_player_size.y / 2):
            if self.player_pos.x + movement.x < (self.window.width - (self.total_player_size.x / 2)) and self.player_pos.y + movement.y < (self.window.height - (self.total_player_size.y / 2)):
                self.player_pos += movement

    def still(self):
        self.velocity = vector.Vector(0, 0)

state = State()
