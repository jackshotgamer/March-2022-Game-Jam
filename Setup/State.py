import arcade
from Setup import vector


class State:
    def __init__(self):
        self.player_pos = vector.Vector(0, 0)
        player_size = 0.142857143
        self.player_size_mult = player_size * 4
        self.total_player_size = (vector.Vector(231, 350) * self.player_size_mult) * (1920, 1080)
        self.player_head_size = (vector.Vector(231, 161) * self.player_size_mult) * (1920, 1080)
        self.player_body_size = (vector.Vector(126, 189) * self.player_size_mult) * (1920, 1080)
        self.window = None
        self.velocity = vector.Vector(0, 0)
        self.current_clothes = '2'

    @property
    def screen_center(self):
        return vector.Vector(self.window.width / 2, self.window.height / 2)

    @property
    def player_bounds(self):
        return (vector.Vector(self.player_pos.x - (self.total_player_size.x / 2),
                              self.player_pos.y - (self.total_player_size.y / 2)),
                vector.Vector(self.player_pos.x + (self.total_player_size.x / 2),
                              self.player_pos.y + (self.total_player_size.y / 2)))

    def update_player_pos(self, x, y):
        self.player_pos = vector.Vector(x, y)
        player_size = 0.142857143
        self.player_size_mult = player_size * 4
        self.total_player_size = (vector.Vector(231, 350) * self.player_size_mult) * (self.window.width / 1920, self.window.height / 1080)
        self.player_head_size = (vector.Vector(231, 161) * self.player_size_mult) * (self.window.width / 1920, self.window.height / 1080)
        self.player_body_size = (vector.Vector(126, 189) * self.player_size_mult) * (self.window.width / 1920, self.window.height / 1080)

    def move(self, velocity, sprinting=False):
        if sprinting:
            self.velocity = velocity * 4
        else:
            self.velocity = velocity * 2

    def move_player(self, time_delta):
        movement = self.velocity * time_delta
        if not (self.player_pos.x + movement.x - (self.total_player_size.x / 2) >= 0 and self.player_pos.x + movement.x + (self.total_player_size.x / 2) <= self.window.width):
            movement = movement.copy(x=0)
        if not (self.player_pos.y + movement.y - (self.total_player_size.y / 2) >= 0 and self.player_pos.y + movement.y + (self.total_player_size.y / 2) <= self.window.height):
            movement = movement.copy(y=0)
        self.player_pos += movement

    def still(self):
        self.velocity = vector.Vector(0, 0)


state = State()
