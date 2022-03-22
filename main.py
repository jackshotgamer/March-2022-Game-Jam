import arcade
from Views import menu
from Setup import State

window = arcade.Window(resizable=True, antialiasing=True)
State.state.window = window
State.state.update_player_pos(State.state.screen_center.x + (State.state.screen_center.x / 2), State.state.screen_center.y)
window.show_view(menu.Menu())

if __name__ == '__main__':
    arcade.run()
