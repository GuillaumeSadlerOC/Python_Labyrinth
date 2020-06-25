# -*- coding: utf-8 -*-
""" Labyrinth interface

### REQUIREMENTS
> Pygame 1.9.6

#### DOCUMENTATIONS
! For more informations about this app, consult : README.md
Pygame : https://www.pygame.org/docs/
Pygame display : https://www.pygame.org/docs/ref/display.html
Pygame mouse : https://www.pygame.org/docs/ref/mouse.html

### MODIFICATIONS
Last modification date : 03/09/2019
By : Guillaume SADLER - https://github.com/GRELDAS

"""

# pylint: disable=wildcard-import
# pylint: disable=undefined-variable
# pylint: disable=unused-wildcard-import
# pylint: disable=too-many-instance-attributes

# LIBRARY IMPORTS
import pygame.display
import pygame.mouse
from pygame.locals import *

# PROGRAM IMPORTS
from frontend.program_interface import ProgramInterface
from settings import TILE_WIDTH
from settings import TILE_HEIGHT


class LabyrinthInterface(ProgramInterface):
    """ Labyrinth interface

    This class can use this ProgramInterface methods :

    > create_surface(interface_name)
    Create pygame Surface of interface.

    > upload_images(img_manager, img_list)
    Pygame upload images.

    > get_buttons(img_manager, img_list)
    Get Pygame rect.

    > start_sound(sound_path)
    Start Pygame mixer sound.

    """

    def __init__(self, program):
        """ Labyrinth interface initialization

        Args:
            program(instance): Instance of Program.

        Attributes:
            img_manager(instance): Instance of ImageManager.
            labyrinth_buttons(list): List of Pygame rect.
            labyrinth_surface(surface): Pygame surface.
            background_color(tuple): RGB color.
            labyrinth_sound(str): Path to defeat sound.
            img_tiles(list): Labyrinth tiles images.
            img_items(list): Labyrinth items images.
            img_characters(list): Labyrinth characters images.
            menu_elements(list): Labyrinth menu images.
            tile_width(int): Labyrinth tiles width.
            tile_height(int): Labyrinth tiles height.
            game(instance): Instance of Game.

        """

        # Args
        self.program = program

        # Attributes
        self.img_manager = self.program.img_manager
        self.labyrinth_buttons = None
        self.labyrinth_surface = None
        self.background_color = 52, 52, 52
        self.labyrinth_sound = 'static/sounds/piste_audio.mp3'

        self.img_tiles = [
            {
                'address': 'static/images/labyrinth/tiles/',
                'name': 'fire',
                'format': 'png',
                'rect': False
            },
            {
                'address': 'static/images/labyrinth/tiles/',
                'name': 'path',
                'format': 'png',
                'rect': False
            },
            {
                'address': 'static/images/labyrinth/tiles/',
                'name': 'wall',
                'format': 'png',
                'rect': False
            },
            {
                'address': 'static/images/labyrinth/tiles/',
                'name': 'wall0',
                'format': 'png',
                'rect': False
            },
            {
                'address': 'static/images/labyrinth/tiles/',
                'name': 'wall1',
                'format': 'png',
                'rect': False
            },
            {
                'address': 'static/images/labyrinth/tiles/',
                'name': 'wall2',
                'format': 'png',
                'rect': False
            },
            {
                'address': 'static/images/labyrinth/tiles/',
                'name': 'wall3',
                'format': 'png',
                'rect': False
            },
            {
                'address': 'static/images/labyrinth/tiles/',
                'name': 'wall4',
                'format': 'png',
                'rect': False
            },
            {
                'address': 'static/images/labyrinth/tiles/',
                'name': 'wall5',
                'format': 'png',
                'rect': False
            },
            {
                'address': 'static/images/labyrinth/tiles/',
                'name': 'wall6',
                'format': 'png',
                'rect': False
            },
            {
                'address': 'static/images/labyrinth/tiles/',
                'name': 'wall7',
                'format': 'png',
                'rect': False
            },
            {
                'address': 'static/images/labyrinth/tiles/',
                'name': 'wall8',
                'format': 'png',
                'rect': False
            },
            {
                'address': 'static/images/labyrinth/tiles/',
                'name': 'wall9',
                'format': 'png',
                'rect': False
            }
        ]

        self.img_items = [
            {
                'address': 'static/images/labyrinth/items/',
                'name': 'armor',
                'format': 'png',
                'rect': False
            },
            {
                'address': 'static/images/labyrinth/items/',
                'name': 'key',
                'format': 'png',
                'rect': False
            },
            {
                'address': 'static/images/labyrinth/items/',
                'name': 'sword',
                'format': 'png',
                'rect': False
            },
            {
                'address': 'static/images/labyrinth/items/',
                'name': 'life',
                'format': 'png',
                'rect': False
            },
            {
                'address': 'static/images/labyrinth/items/',
                'name': 'treasure',
                'format': 'png',
                'rect': False
            }
        ]

        self.img_characters = [
            {
                'address': 'static/images/labyrinth/characters/',
                'name':'character',
                'format': 'png',
                'rect': False
            },
            {
                'address': 'static/images/labyrinth/characters/',
                'name':'guardian',
                'format': 'png',
                'rect': False
            }
        ]

        self.menu_elements = [
            {
                'address': 'static/images/labyrinth/menu/',
                'name': 'armor_off',
                'format': 'png',
                'rect': False
            },
            {
                'address': 'static/images/labyrinth/menu/',
                'name': 'armor_on',
                'format': 'png',
                'rect': False
            },
            {
                'address': 'static/images/labyrinth/menu/',
                'name': 'key_off',
                'format': 'png',
                'rect': False
            },
            {
                'address': 'static/images/labyrinth/menu/',
                'name': 'key_on',
                'format': 'png',
                'rect': False
            },
            {
                'address': 'static/images/labyrinth/menu/',
                'name': 'sword_off',
                'format': 'png',
                'rect': False
            },
            {
                'address': 'static/images/labyrinth/menu/',
                'name': 'sword_on',
                'format': 'png',
                'rect': False
            },
            {
                'address': 'static/images/labyrinth/menu/',
                'name': 'life_1',
                'format': 'png',
                'rect': False
            },
            {
                'address': 'static/images/labyrinth/menu/',
                'name': 'life_2',
                'format': 'png',
                'rect': False
            },
            {
                'address': 'static/images/labyrinth/menu/',
                'name': 'life_3',
                'format': 'png',
                'rect': False
            },
            {
                'address': 'static/images/labyrinth/menu/',
                'name': 'life_4',
                'format': 'png',
                'rect': False
            },
            {
                'address': 'static/images/labyrinth/menu/',
                'name': 'life_5',
                'format': 'png',
                'rect': False
            },
            {
                'address': 'static/images/labyrinth/menu/',
                'name': 'game_retry_button',
                'format': 'png',
                'rect': True,
                'pos_x': 280,
                'pos_y': 620
            },
            {
                'address': 'static/images/labyrinth/menu/',
                'name': 'game_quit_button',
                'format': 'png',
                'rect': True,
                'pos_x': 280,
                'pos_y': 650
            }
        ]

        self.tile_width = TILE_WIDTH
        self.tile_height = TILE_HEIGHT
        self.game = self.program.game

        self.labyrinth_initialization()

    def labyrinth_initialization(self):
        """ Labyrinth initialization """

        self.labyrinth_surface = self.create_surface(
            interface_name='Pygame Labyrinth - niveau {}'.format(
                1
            )
        )

        # Upload labyrinth tiles
        self.upload_images(
            img_manager=self.img_manager,
            img_list=self.img_tiles
        )

        # Upload labyrinth items
        self.upload_images(
            img_manager=self.img_manager,
            img_list=self.img_items
        )

        # Upload labyrinth items
        self.upload_images(
            img_manager=self.img_manager,
            img_list=self.img_characters
        )

        # Upload labyrinth menu
        self.upload_images(
            img_manager=self.img_manager,
            img_list=self.menu_elements
        )

        # Get labyrinth buttons
        self.labyrinth_buttons = self.get_buttons(
            img_manager=self.img_manager,
            img_list=self.menu_elements
        )

        # Get sound
        self.start_sound(
            sound_path=self.labyrinth_sound
        )

    def display_menu(self):
        """ Display the game menu """

        # Display the remaining life
        life_img = "life_{}".format(
            self.game.remaining_life
        )

        self.img_manager.images_blit(
            img_name=life_img,
            surface=self.labyrinth_surface,
            pos_x=5,
            pos_y=620
        )

        # Display the recovery status of armor
        if self.game.armor == 0:
            armor_img = "armor_off"
        else:
            armor_img = "armor_on"

        self.img_manager.images_blit(
            img_name=armor_img,
            surface=self.labyrinth_surface,
            pos_x=80,
            pos_y=620
        )

        # Display the recovery status of key
        if self.game.key == 0:
            key_img = "key_off"
        else:
            key_img = "key_on"

        self.img_manager.images_blit(
            img_name=key_img,
            surface=self.labyrinth_surface,
            pos_x=155,
            pos_y=620
        )


        # Display the recovery status of sword
        if self.game.sword == 0:
            sword_img = "sword_off"
        else:
            sword_img = "sword_on"

        self.img_manager.images_blit(
            img_name=sword_img,
            surface=self.labyrinth_surface,
            pos_x=220,
            pos_y=620
        )

        # Display the game menu buttons
        self.img_manager.images_blit(
            img_name="game_retry_button",
            surface=self.labyrinth_surface,
            pos_x=300,
            pos_y=620
        )

        self.img_manager.images_blit(
            img_name="game_quit_button",
            surface=self.labyrinth_surface,
            pos_x=300,
            pos_y=650
        )

    @classmethod
    def transform_type(cls, tile):
        """ Return the image name of a type

        Args:
            tile(str): Tile content.

        Return:
            image name.

        """

        images = [
            {
                'name': 'wall',
                'tile': 'x'
            },
            {
                'name': 'wall0',
                'tile': '0'
            },
            {
                'name': 'wall1',
                'tile': '1'
            },
            {
                'name': 'wall2',
                'tile': '2'
            },
            {
                'name': 'wall3',
                'tile': '3'
            },
            {
                'name': 'wall4',
                'tile': '4'
            },
            {
                'name': 'wall5',
                'tile': '5'
            },
            {
                'name': 'wall6',
                'tile': '6'
            },
            {
                'name': 'wall7',
                'tile': '7'
            },
            {
                'name': 'wall8',
                'tile': '8'
            },
            {
                'name': 'wall9',
                'tile': '9'
            },
            {
                'name': 'path',
                'tile': 'c'
            },
            {
                'name': 'fire',
                'tile': 'f'
            },
            {
                'name': 'life',
                'tile': 'l'
            },
            {
                'name': 'armor',
                'tile': 'a'
            },
            {
                'name': 'key',
                'tile': 'k'
            },
            {
                'name': 'sword',
                'tile': 's'
            },
            {
                'name': 'character',
                'tile': 'P'
            },
            {
                'name': 'guardian',
                'tile': 'A'
            },
        ]

        for image in images:

            if image['tile'] == tile:
                name_image = image['name']

        return name_image

    def display_labyrinth(self):
        """ Display the labyrinth """

        line_number = 0 # X
        column_number = 0 # Y

        tile = ""
        blit_path = 0

        for labyrinth_line in self.program.game.labyrinth:

            for labyrinth_tile in labyrinth_line:

                tile = labyrinth_tile

                if column_number == len(self.program.game.labyrinth):
                    column_number = 0

                name_image = self.transform_type(tile=tile)

                if name_image == "life":
                    blit_path += 1
                elif name_image == "armor":
                    blit_path += 1
                elif name_image == "key":
                    blit_path += 1
                elif name_image == "sword":
                    blit_path += 1
                elif name_image == "character":
                    blit_path += 1
                elif name_image == "guardian":
                    blit_path += 1

                if blit_path == 1:

                    self.img_manager.images_blit(
                        img_name="path",
                        surface=self.labyrinth_surface,
                        pos_x=column_number * self.tile_width,
                        pos_y=line_number * self.tile_height
                    )

                    self.img_manager.images_blit(
                        img_name=name_image,
                        surface=self.labyrinth_surface,
                        pos_x=column_number * self.tile_width,
                        pos_y=line_number * self.tile_height
                    )

                    blit_path = 0

                else:

                    self.img_manager.images_blit(
                        img_name=name_image,
                        surface=self.labyrinth_surface,
                        pos_x=column_number * self.tile_width,
                        pos_y=line_number * self.tile_height
                    )

                column_number += 1

            line_number += 1

    def display(self):
        """ Display the labyrinth interface """

        self.labyrinth_surface.fill(
            self.background_color
        )

        self.display_labyrinth()
        self.display_menu()

        pygame.display.flip()

    def event_loop(self, event):
        """ Event loop

        Args:
            event(Instance): Instance of Pygame Event.

        """

        if event.type == MOUSEBUTTONDOWN:

            mouse_pos = pygame.mouse.get_pos()

            for button in self.labyrinth_buttons:

                if button['rect'].collidepoint(mouse_pos):

                    if button['name'] == 'game_retry_button':
                        self.program.new_game(
                            level=self.program.game.level
                        )

                    elif button['name'] == 'game_quit_button':
                        quit()

        if event.type == KEYDOWN:

            if event.key == K_RIGHT:
                self.game.movement_collusion("right")
            elif event.key == K_LEFT:
                self.game.movement_collusion("left")
            elif event.key == K_UP:
                self.game.movement_collusion("up")
            elif event.key == K_DOWN:
                self.game.movement_collusion("down")
