from unittest import TestCase
from mock import Mock, MagicMock, patch

from figures.figures.figure_creator import CircleCreator


class TestFigures(TestCase):

    def setUp(self):
        self.circle = CircleCreator('Circle')

    def tearDown(self):
        self.circle = None

    def test_name_ok(self):
        self.assertEqual(self.circle.get_name(), 'Circle')

    @patch.object(CircleCreator, '_compute_area')
    def test_default_area_ok(self, compute_area_patch):
        compute_area_patch.return_value = 0
        self.assertEqual(self.circle.get_properties()['area'], 0)

    @patch('random.random')
    def test_compute_area(self, r_patch):
        r_patch.return_value = 0
        self.assertEqual(self.circle.get_properties()['area'], 0)

    def test_change_area_ok(self):
        self.circle.set_area(4)
        assert self.circle.area == 4

    def test_mocked_circle(self):
        circle = MagicMock()
        print ('circle: ' + str(circle.get_name()))
        assert circle.get_name() != ''
