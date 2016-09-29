import random

from figures.figures.figure_patterns import FigurePatterns

class CircleCreator(FigurePatterns, object):

    LINE_WIDTH = 5

    def __init__(self, name, perimeter=7):
        super(CircleCreator, self).__init__(name)
        self.perimeter = perimeter

    def get_properties(self):
        return {'name': self.name, 'area': self._compute_area(), 'perimeter': self.get_perimeter()}
    
    def _compute_area(self):
        return random.random()*10

    def set_perimeter(self, value):
        self.perimeter = value

    def get_perimeter(self):
        return self.perimeter

class SquareCreator(FigurePatterns):

    LINE_WIDTH = 2

    def __init__(self, name):
        super(SquareCreator, self).__init__(name)
