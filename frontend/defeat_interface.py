# -*- coding: utf-8 -*-
""" Defeat interface

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


class DefeatInterface(ProgramInterface):
    """ Defeat interface

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
        """ Defeat interface initialization

        Args:
            program(instance): Instance of Program.

        Attributes:
            img_manager(instance): Instance of ImageManager.
            defeat_buttons(list): List of Pygame rect.
            defeat_surface(surface): Pygame surface.
            background_color(tuple): RGB color.
            defeat_sound(str): Path to defeat sound.
            images_list(list): Interface images.

        """

        # Args
        self.program = program

        # Attributes
        self.img_manager = self.program.img_manager
        self.defeat_buttons = None
        self.defeat_surface = None
        self.background_color = 255, 255, 255
        self.defeat_sound = 'static/sounds/defeat.wav'
        self.defeat_images_list = [
            {
                'address': 'static/images/defeat/',
                'name': 'defeat_retry_button',
                'format': 'png',
                'rect': True,
                'pos_x': 140,
                'pos_y': 180
            },
            {
                'address': 'static/images/defeat/',
                'name': 'defeat_quit_button',
                'format': 'png',
                'rect': True,
                'pos_x': 140,
                'pos_y': 239
            },
        ]

        self.defeat_initialization()

    def defeat_initialization(self):
        """ Defeat initialization """

        self.defeat_surface = self.create_surface(
            interface_name='Pygame Labyrinth - Defaite !'
        )

        # Upload defeat images
        self.upload_images(
            img_manager=self.img_manager,
            img_list=self.defeat_images_list
        )

        # Get defeat buttons
        self.defeat_buttons = self.get_buttons(
            img_manager=self.img_manager,
            img_list=self.defeat_images_list
        )

    def display(self):
        """ Display the defeat interface """

        self.defeat_surface.fill(
            self.background_color
        )

        for image in self.defeat_images_list:

            self.img_manager.images_blit(
                img_name=image['name'],
                surface=self.defeat_surface,
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

            for button in self.defeat_buttons:

                if button['rect'].collidepoint(mouse_pos):

                    if button['name'] == 'defeat_retry_button':
                        self.program.new_game()

                    elif button['name'] == 'defeat_quit_button':
                        quit()
