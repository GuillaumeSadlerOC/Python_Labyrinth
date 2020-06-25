# -*- coding: utf-8 -*-
""" Labyrinth

This module transform a string who represent labyrinth into
a list of lists for manipulations.

### REQUIREMENTS
> random of Python 3.6

#### DOCUMENTATIONS
! For more informations about this app, consult : README.md
Python Random : https://docs.python.org/3.6/library/random.html

### MODIFICATIONS
Last modification date : 02/09/2019
By : Guillaume SADLER - https://github.com/GRELDAS

"""

# LIBRARY IMPORTS
from random import randrange


class Labyrinth():
    """ Construct labyrinth

    This class is instanciated by an instance of Game.

    """

    items = {
        'armor': 'a',
        'key': 'k',
        'sword': 's'
    }

    levels = [
        {
            'items':{
                'armor': 'a',
                'key': 'k',
                'sword': 's'
            }
        },
        {
            'items':{
                'armor': 'a',
                'key': 'k',
                'sword': 's'
            }
        }
    ]

    def __init__(self, level):
        """ Labyrinth initialization

        Args:
            level(int): Labyrinth level.

        """

        self.labyrinth = self.get_labyrinth(
            level=level
        )

    def get_labyrinth(self, level):
        """ Level construct

        Construct labyrinth level.

        Args:
            level(int): Labyrinth level.

        """

        labyrinth = self.get_labyrinth_list(
            level=level
        )

        new_labyrinth = self.add_items(
            level=level,
            labyrinth=labyrinth
        )

        return new_labyrinth

    @classmethod
    def get_labyrinth_list(cls, level):
        """ Get labyrinth

        Transform txt to list of lists who represent labyrinth.

        Args:
            level(int): Labyrinth level.

        Return:
            new_labyrinth(list): list of lists.

        """

        new_labyrinth = []

        labyrinth_path = "backend/labyrinths/level-{}.txt".format(
            level
        )

        with open(labyrinth_path, "r") as laby_file:
            labyrinth_txt = laby_file.read()

        for loop_1 in labyrinth_txt.split('\n'):
            line = []
            for tile in loop_1:
                line.append(tile)
            new_labyrinth.append(line)

        return new_labyrinth

    def add_items(self, level, labyrinth):
        """ Add items

        Args:
            level(int): Labyrinth level.
            labyrinth(list): list of lists.

        Return:
            labyrinth(list): labyrinth with items.

        """

        level = level - 1

        level_items = self.levels[int(level)]

        for level_item in level_items['items']:

            line_number = randrange(len(labyrinth))
            col_number = randrange(len(labyrinth))

            while labyrinth[line_number][col_number] != 'c':

                line_number = randrange(len(labyrinth))
                col_number = randrange(len(labyrinth))

            labyrinth[line_number][col_number] = self.items[level_item]

        return labyrinth
