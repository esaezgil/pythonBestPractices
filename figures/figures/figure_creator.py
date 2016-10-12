import random

from figures.figures.figure_patterns import FigurePatterns


class CircleCreator(FigurePatterns, object):

    LINE_WIDTH = 5

    def __init__(self, name, area=7):
        super(CircleCreator, self).__init__(name)
        self.area = area

    def get_properties(self):
        return {'name': self.name, 'area': self._compute_area()}

    def _compute_area(self):
        return random.random()*10

    def set_area(self, value):
        self.area = value

    def get_area(self):
        return self.area


class SquareCreator(FigurePatterns):

    LINE_WIDTH = 2

    def __init__(self, name):
        super(SquareCreator, self).__init__(name)
