# -*- coding: utf-8 -*-
""" Game

### REQUIREMENTS
> Pygame 1.9.6

#### DOCUMENTATIONS
! For more informations about this app, consult : README.md
Pygame docs : https://www.pygame.org/docs/
Pygame mixer : https://www.pygame.org/docs/ref/mixer.html

### MODIFICATIONS
Last modification date : 03/09/2019
By : Guillaume SADLER - https://github.com/GRELDAS

"""

# pylint: disable=too-many-instance-attributes
# pylint: disable=too-many-branches

# LIBRARY IMPORTS
import pygame.mixer

# PROGRAM IMPORTS
from backend.labyrinth import Labyrinth
from settings import LEVELS

class Game():
    """ Game

    This class is instanciated by an instance of Program.
    (new_game method)

    """

    def __init__(self, program, level):
        """ Game initialization

            Args:
                program(instance): Program instance.
                level(int): Game level.

            Params:
                remaining_life(int): Player remaining life.
                armor(int): Player item quantity.
                key(int): Player key quantity.
                sword(int): Player sword quantity.
                items(int): Player item quantity.
                line_number(int): Pos X of player in labyrinth.
                column_number(int): Pos Y of player in labyrinth.
                labyrinth(list): List of lists who represent labyrinth.

        """

        # Args
        self.program = program
        self.level = level

        # Params
        self.remaining_life = 5
        self.armor = 0
        self.key = 0
        self.sword = 0
        self.items = 0
        self.line_number = 0
        self.column_number = 0
        self.labyrinth = Labyrinth(
            level=self.level
        ).labyrinth

    def movement_collusion(self, movement_name):
        """ Movement collusion test

        Test the sprite where wish to move the player

        Args:
            movement(str) : Movement name of the character.

        Params:
            line_number(int) : line where the character is / Then he will be
            column_number(int) : column where the character is / Then he will be

        """

        line_number = self.line_number
        column_number = self.column_number

        # 1 : We calculate the sprite where wish to move the player
        if movement_name == "right":
            column_number += 1
        elif movement_name == "left":
            column_number -= 1
        elif movement_name == "down":
            line_number += 1
        elif movement_name == "up":
            line_number -= 1

        # 2 : We test that we don't leave the frame of the labyrinth
        if movement_name == "right" and column_number <= 14:
            sprite_content = self.labyrinth[
                line_number
            ][column_number]
        elif movement_name == "left" and column_number >= 0:
            sprite_content = self.labyrinth[
                line_number
            ][column_number]
        elif movement_name == "down" and line_number <= 14:
            sprite_content = self.labyrinth[
                line_number
            ][column_number]
        elif movement_name == "up" and line_number >= 0:
            sprite_content = self.labyrinth[
                line_number
            ][column_number]
        else:
            sprite_content = "offFields"

        # 3 : Take an action based on the result of the previous tests

        if sprite_content == "offFields":
            pass
        # Sprite points to a wall
        elif sprite_content == "x":
            pass
        # Sprite points to a path
        elif sprite_content == "c":
            self.movement(movement_name)
        # Sprite points to a fire path
        elif sprite_content == "f":
            self.game_result("fire")
        # Sprite points to an life
        elif sprite_content == "l":
            self.add_item("l")
            self.movement(movement_name)
        # Sprite points to an armor item
        elif sprite_content == "a":
            self.add_item("a")
            self.movement(movement_name)
        # Sprite points to an sword item
        elif sprite_content == "s":
            self.add_item("s")
            self.movement(movement_name)
        # Sprite points to an key item
        elif sprite_content == "k":
            self.add_item("k")
            self.movement(movement_name)
        # Sprite points on the arrival
        elif sprite_content == "A":
            self.game_result("arrival")

    def movement(self, movement_name):
        """ Movement of character

        Manage character moves

        Args:
            movement_name(str) : Movement name of the character.
            (Right, left, down or start.)

        """

        # 1 : We modify the sprite where the character is located before moving
        self.labyrinth[
            self.line_number
        ][self.column_number] = "c"

        # 2 : We calculate the sprite where move the player

        if movement_name == "right":
            self.column_number += 1
        elif movement_name == "left":
            self.column_number -= 1
        elif movement_name == "down":
            self.line_number += 1
        elif movement_name == "up":
            self.line_number -= 1
        elif movement_name == "start":
            self.line_number = 0
            self.column_number = 0

        # 3 : We modify the sprite on which we juste moved the character
        self.labyrinth[
            self.line_number
        ][self.column_number] = "P"

    def add_item(self, item_type):
        """ Add item

        Args:
            item_type (int) : Type of the item to "pick up"

        """

        item_type = item_type

        # Armor
        if item_type == "a":
            self.items += 1
            self.armor += 1
        # Key
        elif item_type == "k":
            self.items += 1
            self.key += 1
        # Sword
        elif item_type == "s":
            self.items += 1
            self.sword += 1
        # Life
        elif item_type == "l":

            if self.remaining_life < 5:
                self.remaining_life += 1

    def game_result(self, values):
        """ Game result

        Victory or defeat.

        Args:
            values(str) : 'arrival' or 'fire'

        """

        result_game = values

        # if the player shows up on the finish square
        if result_game == "arrival":

            # if the player to pick up the 3 objects / He win
            if self.items < 3:

                self.program.active_interface = self.program.defeat_interface
                self.program.defeat = True

            elif self.items == 3:

                if self.program.game.level < LEVELS:
                    self.program.active_interface = self.program.win_interface
                    self.program.game.win = True
                else:
                    pygame.mixer.music.stop()
                    self.program.active_interface = self.program.home_interface

        # if the player has walked on fire
        elif result_game == "fire":

            # if the player has no more life / He dies
            if self.remaining_life == 1:
                self.program.active_interface = self.program.defeat_interface
            else:

                # the player lose one life point
                self.remaining_life -= 1

                # the player returns on the start square
                self.movement("start")
