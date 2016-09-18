import random

from figures.figures.figure_patterns import FigureStructure

class CircleCreator(FigureStructure, object):

    LINE_WIDTH = 5

    def __init__(self, name, perimeter=0):
        super(CircleCreator, self).__init__(name)
        self.perimeter = perimeter
    
    def get_properties(self):
        return {'name': self.name, 'perimeter': self._compute_perimeter()}
    
    def _compute_perimeter(self):
        return random.random()*10

    def set_perimeter(self, value):
        self.perimeter = value

class SquareCreator(FigureStructure):

    LINE_WIDTH = 2

    def __init__(self, name):
        super(SquareCreator, self).__init__(name)


	
