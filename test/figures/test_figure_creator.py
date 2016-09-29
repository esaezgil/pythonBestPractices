from unittest import TestCase
from mock import Mock, MagicMock, patch

from figures.figures.figure_creator import CircleCreator, SquareCreator


class TestFigureCreator(TestCase):

    def setUp(self):
        self.circle = CircleCreator('Circle')
        self.square = SquareCreator('Square')

    def test_figure_creator(self):
        assert self.circle.LINE_WIDTH == 5
        assert self.circle.TRANSPARENCY == 15
        assert self.square.LINE_WIDTH == 2
        assert self.square.TRANSPARENCY == 15

    @patch.object(CircleCreator, '_compute_area')
    def test_default_perimeter_ok(self, compute_perimeter_patch):
        compute_perimeter_patch.return_value = 0
        self.assertEqual(self.circle.get_properties()['area'], 0)

    @patch('random.random')
    def test_compute_perimeter(self, random_patch):
        random_patch.return_value = 0
        self.assertEqual(self.circle.get_properties()['area'], 0)

    @patch('random.random')
    def test_circle_creator(self, random_patch):
        random_patch.return_value = 0
        circle = CircleCreator('circle', perimeter=5)
        assert circle.get_name() == 'circle'
        assert circle.get_properties().get('area') == 0

    def test_set_perimeter(self):
        self.circle.set_perimeter(5)
        assert self.circle.get_properties().get('perimeter') == 5

    def test_mocked_circle(self):
        circle = Mock()
        circle.get_name.return_value = 'circle_mock'
        assert circle.get_name() == 'circle_mock'