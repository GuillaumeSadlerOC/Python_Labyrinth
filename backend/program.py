# -*- coding: utf-8 -*-
""" Program

### REQUIREMENTS
> Pygame 1.9.6

#### DOCUMENTATIONS
! For more informations about this app, consult : README.md
Pygame : https://www.pygame.org/docs/
Pygame event : https://www.pygame.org/docs/ref/event.html

### MODIFICATIONS
Last modification date : 02/09/2019
By : Guillaume SADLER - https://github.com/GRELDAS

"""

# pylint: disable=too-many-instance-attributes

# LIBRARY IMPORTS
import pygame.event

# PROGRAM IMPORTS
from backend.game import Game
from frontend.home_interface import HomeInterface
from frontend.labyrinth_interface import LabyrinthInterface
from frontend.defeat_interface import DefeatInterface
from frontend.win_interface import WinInterface
from frontend.image_manager import ImageManager

class Program():
    """ Program """

    def __init__(self):
        """ Program initialization

        Attributes:
            program_quit(bool): Define the status of program.
            img_manager(instance): Instance of ImageManager.
            home_interface(instance): Instance of HomeInterface.
            labyrinth_interface(instance): Instance of LabyrinthInterface.
            win_interface(instance): Instance of WinInterface.
            defeat_interface(instance): Instance of DefeatInterface.
            active_interface(instance): Instance of interface to display.
            game(instance): Instance of Game.

        """

        # Attributes
        self.program_quit = False
        self.img_manager = None
        self.home_interface = None
        self.labyrinth_interface = None
        self.win_interface = None
        self.defeat_interface = None
        self.active_interface = None
        self.game = None

        self.program_initialization()

    def program_initialization(self):
        """ Program initialization """

        self.img_manager = ImageManager()

        self.defeat_interface = DefeatInterface(
            program=self
        )

        self.win_interface = WinInterface(
            program=self
        )

        self.home_interface = HomeInterface(
            program=self
        )

        # Display home interface
        self.active_interface = self.home_interface

    def program_loop(self):
        """ Program loop """

        while not self.program_quit:

            self.event_loop()
            self.active_interface.display()

    def event_loop(self):
        """ Event loop """

        for event in pygame.event.get():

            # EVENT 1 : QUIT
            if event.type == pygame.QUIT:
                quit()

            self.active_interface.event_loop(
                event=event
            )

    def new_game(self, level=1):
        """ new game

        Construct new labyrinth game.

        Args:
            level(int): Game level to construct.

        """

        self.game = Game(
            program=self,
            level=level
        )

        self.labyrinth_interface = LabyrinthInterface(
            program=self
        )

        self.active_interface = self.labyrinth_interface
