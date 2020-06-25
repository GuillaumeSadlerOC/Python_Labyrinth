# -*- coding: utf-8 -*-
""" Program interface

### REQUIREMENTS
> Pygame 1.9.6

#### DOCUMENTATIONS
! For more informations about this app, consult : README.md
Pygame : https://www.pygame.org/docs/
Pygame display : https://www.pygame.org/docs/ref/display.html
Pygame mixer : https://www.pygame.org/docs/ref/mixer.html

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
import pygame.mixer

# PROGRAM IMPORTS
from settings import WINDOW_WIDTH
from settings import WINDOW_HEIGHT


class ProgramInterface():
    """ Program interface

    This class is inherited by :
    - HomeInterface
    - LabyrinthInterface
    - WinInterface
    - DefeatInterface

    """

    @classmethod
    def create_surface(cls, interface_name):
        """ Create pygame Surface of interface.

        Args:
            interface_name(str): Interface name.

        Return:
            Pygame surface.

        """

        pygame.display.init()

        pygame.display.set_caption(
            interface_name
        )

        window_surface = pygame.display.set_mode(
            (WINDOW_WIDTH, WINDOW_HEIGHT)
        )

        return window_surface

    @classmethod
    def upload_images(cls, img_manager, img_list):
        """ Pygame upload images

        Args:
            img_manager(instance): Instance of ImageManager.
            img_list(list): Interface images.

        """

        for image in img_list:

            img_manager.images_upload(
                image=image
            )

    @classmethod
    def get_buttons(cls, img_manager, img_list):
        """ Get Pygame rect.

        Args:
            img_manager(instance): Instance of ImageManager.
            img_list(list): Interface images.

        Return:
            List of Pygame rect who represent buttons.

        """

        buttons = []

        for image in img_list:

            if image['rect']:

                image_rect = img_manager.get_image(
                    image_name=image['name']
                )

                buttons.append(image_rect)

        return buttons

    @classmethod
    def start_sound(cls, sound_path):
        """ Start Pygame mixer sound.

        Args:
            sound_path(str): Path of sound to load.

        """

        pygame.mixer.init()

        pygame.mixer.music.load(
            sound_path
        )

        # Volume adjustment
        pygame.mixer.music.set_volume(
            0.1
        )

        pygame.mixer.music.play()
