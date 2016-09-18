from collections import namedtuple


LINE_WIDTH = 3

class FigureStructure(object):
         
    TRANSPARENCY = 0    

    def __init__(self, name, transparency=TRANSPARENCY):
        self.name = name
    
    def get_name(self):
        return self.name
    
    def get_line_width(self):
        return LINE_WIDTH



    
    
