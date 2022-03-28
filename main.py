import arcade
from Views import Game
from Setup import State

window = arcade.Window(1620, 911, resizable=False, antialiasing=True)
State.state.window = window
State.state.update_player_pos(State.state.screen_center.x + (State.state.screen_center.x / 2), State.state.screen_center.y)
window.show_view(Game.Game())

if __name__ == '__main__':
    arcade.run()
