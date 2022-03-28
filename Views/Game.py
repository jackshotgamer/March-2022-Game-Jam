import arcade
import time
from Setup import sprites, vector, State, hashgrid, Interactables
import random


class Game(arcade.View):
    def __init__(self):
        super().__init__()
        self.state = State
        arcade.set_background_color((139, 69, 19, 150))
        self.pressed_wasd = {
            arcade.key.W: False,
            arcade.key.A: False,
            arcade.key.S: False,
            arcade.key.D: False,
            arcade.key.LSHIFT: False,
        }
        self.movement_speed = 100
        self.angle = (random.choice((0, 180)))
        self.previous_window_size = vector.Vector(1120, 630)
        self.last_resize_time = -1
        self.change_size = [0, '']
        self.frame_counter = 0
        self.flipped_body = False
        self.hashg = hashgrid.HashGrid(100)
        self.interactables = [Interactables.Interactable('E', 'TimmyHeadStress0', (vector.Vector(100, 100), vector.Vector(150, 150)), lambda :None)]
        self.hashg.add_liquid(self.interactables[0], self.interactables[0].bounds)

    def on_update(self, delta_time: float):
        self.frame_counter += 1
        if not any(self.pressed_wasd.values()):
            State.state.still()
        if not self.frame_counter % (12 if not self.pressed_wasd[arcade.key.LSHIFT] else 6) and not State.state.velocity.is_zero(.00001):
            self.flipped_body = not self.flipped_body
            self.frame_counter = 1
        State.state.move(vector.Vector((self.movement_speed if self.pressed_wasd[arcade.key.D] else (-self.movement_speed if self.pressed_wasd[arcade.key.A] else 0)),
                                       (self.movement_speed if self.pressed_wasd[arcade.key.W] else (-self.movement_speed if self.pressed_wasd[arcade.key.S] else 0))),
                         self.pressed_wasd[arcade.key.LSHIFT])
        State.state.move_player(delta_time)
        obj_in_area = self.hashg.get_liquids_box(State.state.player_bounds)
        if obj_in_area:
            distance_x1 = min(State.state.player_pos.x - obj_in_area[0].bounds[0].x, State.state.player_pos.x - obj_in_area[0].bounds[1].x)
            distance_y1 = min(State.state.player_pos.y - obj_in_area[0].bounds[0].y, State.state.player_pos.y - obj_in_area[0].bounds[1].y)
            distance_to_player = vector.Vector(distance_x1, distance_y1)
            print(obj_in_area if distance_to_player.x + distance_to_player.y < obj_in_area[0].size.x else '')
        if self.change_size[1] and (time.time() - self.last_resize_time > 0.5 and self.last_resize_time >= 0):
            if self.change_size[1] == 'width':
                print(self.change_size)
                State.state.window.width = int(self.change_size[0])
            else:
                State.state.window.height = int(self.change_size[0])
            self.change_size = [0, '']
            self.last_resize_time = -1

    def on_resize(self, width: int, height: int):
        self.last_resize_time = time.time()
        if width == self.previous_window_size.x:
            changed = 'height'
            base_num = height
        else:
            changed = 'width'
            base_num = width
        mult = base_num / (16 if changed == 'width' else 9)
        # TODO
        if changed == 'height':
            self.change_size = [16 * mult, 'width']
        else:
            self.change_size = [9 * mult, 'height']
        self.previous_window_size = vector.Vector(width, height)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(State.state.screen_center.x, State.state.screen_center.y, State.state.window.width, State.state.window.height, sprites.load_sprite('FloorBoards'),
                                      angle=self.angle)
        for interactable in self.interactables:
            arcade.draw_texture_rectangle(interactable.center.x, interactable.center.y, interactable.size.x, interactable.size.y, sprites.load_sprite(interactable.sprite))
            arcade.draw_rectangle_outline(interactable.center.x, interactable.center.y, 50, 50, (0, 0, 0), 2)
            arcade.draw_point(interactable.bounds[0].x, interactable.bounds[0].y, (0, 0, 0), 5)
            arcade.draw_point(interactable.bounds[1].x, interactable.bounds[1].y, (0, 0, 0), 5)
        arcade.draw_rectangle_outline(State.state.player_pos.x, State.state.player_pos.y, State.state.total_player_size.x, State.state.total_player_size.y, (0, 0, 0))
        arcade.draw_point(State.state.player_bounds[0].x, State.state.player_bounds[0].y, (0, 0, 0), 5)
        arcade.draw_point(State.state.player_bounds[1].x, State.state.player_bounds[1].y, (0, 0, 0), 5)
        arcade.draw_texture_rectangle(State.state.window.width - 100, 0 + 100, (800 * State.state.player_size_mult) * (State.state.window.width / 1920),
                                      (400 * State.state.player_size_mult) * (State.state.window.height / 1080),
                                      sprites.load_sprite('BedFrame'), -90)
        arcade.draw_texture_rectangle(State.state.player_pos.x, State.state.player_pos.y - (State.state.total_player_size.y * 0.23), State.state.player_body_size.x,
                                      State.state.player_body_size.y,
                                      sprites.load_sprite('TimmyBody' + State.state.current_clothes if not self.flipped_body else 'TimmyBody' + State.state.current_clothes + 'Flip'))
        arcade.draw_texture_rectangle(State.state.player_pos.x, State.state.player_pos.y + (State.state.total_player_size.y * 0.23), State.state.player_head_size.x,
                                      State.state.player_head_size.y, sprites.load_sprite('TimmyHeadStress0'))
        arcade.draw_texture_rectangle(State.state.window.width - 100, 0 + 125, (700 * State.state.player_size_mult) * (State.state.window.width / 1920),
                                      (400 * State.state.player_size_mult) * (State.state.window.height / 1080), sprites.load_sprite('BedSheet'), -90)
        arcade.draw_texture_rectangle(State.state.screen_center.x, 75, 300, 150, sprites.load_sprite('Dresser'))
        arcade.draw_point(State.state.player_pos.x, State.state.player_pos.y, arcade.color.BLACK, 2)

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.G:
            if State.state.current_clothes == '2':
                State.state.current_clothes = '1'
            else:
                State.state.current_clothes = '2'
        if symbol in (arcade.key.W, arcade.key.A, arcade.key.S, arcade.key.D):
            self.pressed_wasd[symbol] = True
        if symbol == arcade.key.LSHIFT:
            self.pressed_wasd[arcade.key.LSHIFT] = True

    def on_key_release(self, _symbol: int, _modifiers: int):
        if _symbol in (arcade.key.W, arcade.key.A, arcade.key.S, arcade.key.D):
            self.pressed_wasd[_symbol] = False
        if _symbol == arcade.key.LSHIFT:
            self.pressed_wasd[arcade.key.LSHIFT] = False
