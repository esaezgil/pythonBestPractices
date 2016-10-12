import json

from figures.figure_creator import CircleCreator, SquareCreator


def main():

    circle = CircleCreator('Circle')
    square = SquareCreator('Square')

    name_circle = json.dumps(circle.get_name())
    name_square = json.dumps(square.get_name())

    circle_properties = circle.get_properties()

    print name_circle
    print circle_properties
    print name_square

if __name__ == "__main__":
    main()
