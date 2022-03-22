import arcade
from Setup import sprites, vector, State


class Menu(arcade.View):
    def __init__(self):
        super().__init__()
        self.state = State
        arcade.set_background_color((200, 200, 200))
        self.pressed_wasd = {
            arcade.key.W: False,
            arcade.key.A: False,
            arcade.key.S: False,
            arcade.key.D: False,
            arcade.key.LSHIFT: False,
        }
        self.movement_speed = 100

    def on_update(self, delta_time: float):
        if not any(self.pressed_wasd.values()):
            State.state.still()
        State.state.move(vector.Vector((self.movement_speed if self.pressed_wasd[arcade.key.D] else (-self.movement_speed if self.pressed_wasd[arcade.key.A] else 0)),
                                       (self.movement_speed if self.pressed_wasd[arcade.key.W] else (-self.movement_speed if self.pressed_wasd[arcade.key.S] else 0))),
                         self.pressed_wasd[arcade.key.LSHIFT])
        State.state.move_player(delta_time)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(State.state.player_pos.x, State.state.player_pos.y + 11.5, State.state.player_head_size.x, State.state.player_head_size.y, sprites.load_sprite('TimmyHeadStress0'))
        arcade.draw_texture_rectangle(State.state.player_pos.x, State.state.player_pos.y - 11.5, State.state.player_body_size.x, State.state.player_body_size.y, sprites.load_sprite('TimmyBody1'))
        arcade.draw_point(State.state.player_pos.x, State.state.player_pos.y, arcade.color.BLACK, 2)

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol in (arcade.key.W, arcade.key.A, arcade.key.S, arcade.key.D):
            self.pressed_wasd[symbol] = True
        if symbol == arcade.key.LSHIFT:
            self.pressed_wasd[arcade.key.LSHIFT] = True

    def on_key_release(self, _symbol: int, _modifiers: int):
        if _symbol in (arcade.key.W, arcade.key.A, arcade.key.S, arcade.key.D):
            self.pressed_wasd[_symbol] = False
        if _symbol == arcade.key.LSHIFT:
            self.pressed_wasd[arcade.key.LSHIFT] = False
