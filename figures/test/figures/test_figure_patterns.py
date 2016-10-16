from unittest import TestCase
from mock import Mock, MagicMock, patch

from figures.figure_patterns import FigurePatterns


class TestFigurePatterns(TestCase):

    def setUp(self):
        self.pattern = FigurePatterns('Pattern')

    def test_pattern(self):
        assert self.pattern.TRANSPARENCY == 15
        assert self.pattern.get_name() == 'Pattern'

    def test_get_transparency(self):
        self.pattern.get_transparency() == 15

    def test_get_name(self):
        assert self.pattern.get_name() == 'Pattern'