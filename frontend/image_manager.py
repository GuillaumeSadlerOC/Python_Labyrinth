# -*- coding: utf-8 -*-
""" Image manager

### REQUIREMENTS
> Pygame 1.9.6

#### DOCUMENTATIONS
! For more informations about this app, consult : README.md
Pygame : https://www.pygame.org/docs/
Pygame image : https://www.pygame.org/docs/ref/image.html

### MODIFICATIONS
Last modification date : 03/09/2019
By : Guillaume SADLER - https://github.com/GRELDAS

"""

# LIBRARY IMPORTS
import pygame.image


class ImageManager():
    """ Image manager

    Creation, storage and reuse images of program.

    Two types of images :
        - the images that will move and that will need a Rect object (buttons).
        - the images that will not move and that will not need a Rect object.

    The goal of this class is to load images once for more program performance.

    """

    def __init__(self):
        """ Image manager initialization

        Attributes:
            images_list(list) : Contains all images objects loaded by Pygame.

        """

        self.images_list = []

    def images_upload(self, image):
        """ Images upload.

        Args:
            image(dict): Image to load if does not exist.

        Example of image dict :

            image = {
                'address': 'static/images/home/',
                'name': 'title',
                'format': 'png',
                'rect': False,
                'pos_x': 60,
                'pos_y': 30
            }

        """

        exist_image = self.get_image(
            image_name=image['name']
        )

        if exist_image is None:

            load_image = {
                'name': '',
                'pygame_image': None,
                'rect': None,
            }

            # 1 : Construct absolute path to the image to load
            path_built = image['address'] + image['name'] + "." + image['format']

            # 2 : Loading the image by pygame
            pygame_image = pygame.image.load(path_built).convert_alpha()

            # 3.1 : Name image storage
            load_image['name'] = image['name']

            # 3.2 : Object Image Pygame storage
            load_image['pygame_image'] = pygame_image

            # OPTIONAL PHASE
            if image['rect']:

                # 4.1 : Creating a Rect object
                img_rect = pygame_image.get_rect()
                img_rect.move_ip(image['pos_x'], image['pos_y'])

                # 4.2 : Rect object storage
                load_image['rect'] = img_rect

            self.images_list.append(load_image)

    def images_blit(self, img_name, surface, pos_x, pos_y):
        """ Images blit

        Copy the image passed as parameter on the display surface.

        Args:
            img_name(str) : Name of the image to display.
            surface(instance) : Instance of Pygame Surface.
            pos_x(int) : Number of pixels to the right
            pos_y(int) : Number of pixels to the down

        """

        # 1 : Recovery of the pygame image object
        pygame_image = self.get_image(
            image_name=img_name
        )['pygame_image']

        # 2 : Copy the image to the surface received as parameter
        surface.blit(pygame_image, (pos_x, pos_y))

    def get_image(self, image_name):
        """ Get image of images_list.

        Args:
            image_name(str): Image name.

        """

        image = None

        for image_dict in self.images_list:

            if image_dict['name'] == image_name:

                image = image_dict

        return image
