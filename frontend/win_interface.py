# -*- coding: utf-8 -*-
""" Win interface

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
# pylint: disable=too-many-nested-blocks

# LIBRARY IMPORTS
import pygame.display
import pygame.mouse
from pygame.locals import *

# PROGRAM IMPORTS
from frontend.program_interface import ProgramInterface
from settings import LEVELS


class WinInterface(ProgramInterface):
    """ Win interface

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
        """ Win interface initialization

        Args:
            program(instance): Instance of Program.

        Attributes:
            img_manager(instance): Instance of ImageManager.
            win_buttons(list): List of Pygame rect.
            win_surface(surface): Pygame surface.
            background_color(tuple): RGB color.
            defeat_sound(str): Path to defeat sound.
            win_images_list(list): Interface images.

        """

        # Args
        self.program = program

        # Attributes
        self.img_manager = self.program.img_manager
        self.win_buttons = None
        self.win_surface = None
        self.background_color = 255, 255, 255
        self.win_sound = 'static/sounds/win.wav'
        self.win_images_list = [
            {
                'address': 'static/images/win/',
                'name': 'next_lvl_button',
                'format': 'png',
                'rect': True,
                'pos_x': 140,
                'pos_y': 301
            },
            {
                'address': 'static/images/win/',
                'name': 'win_retry_button',
                'format': 'png',
                'rect': True,
                'pos_x': 140,
                'pos_y': 360
            },
            {
                'address': 'static/images/win/',
                'name': 'win_quit_button',
                'format': 'png',
                'rect': True,
                'pos_x': 140,
                'pos_y': 419
            },
            {
                'address': 'static/images/win/',
                'name': 'win_display',
                'format': 'png',
                'rect': True,
                'pos_x': 140,
                'pos_y': 80
            }
        ]

        self.win_initialization()

    def win_initialization(self):
        """ Win initialization """

        self.win_surface = self.create_surface(
            interface_name='Pygame Labyrinth - Victoire !'
        )

        # Upload win images
        self.upload_images(
            img_manager=self.img_manager,
            img_list=self.win_images_list
        )

        # Get defeat buttons
        self.win_buttons = self.get_buttons(
            img_manager=self.img_manager,
            img_list=self.win_images_list
        )

    def display(self):
        """ Display the win interface """

        self.win_surface.fill(
            self.background_color
        )

        for image in self.win_images_list:

            self.img_manager.images_blit(
                img_name=image['name'],
                surface=self.win_surface,
                pos_x=image['pos_x'],
                pos_y=image['pos_y'],
            )

        pygame.display.flip()

    def event_loop(self, event):
        """ Event loop

        Args:
            event(Instance): Instance of Pygame Event.

        """

        if event.type == MOUSEBUTTONDOWN:

            mouse_pos = pygame.mouse.get_pos()

            for button in self.win_buttons:

                if button['rect'].collidepoint(mouse_pos):

                    if button['name'] == 'win_retry_button':

                        self.program.new_game(
                            level=self.program.game.level
                        )

                    elif button['name'] == 'next_lvl_button':

                        if self.program.game.level <= LEVELS:

                            if button['rect'].collidepoint(mouse_pos):

                                level = self.program.game.level + 1
                                self.program.new_game(
                                    level=level
                                )

                    elif button['name'] == 'win_quit_button':
                        quit()
