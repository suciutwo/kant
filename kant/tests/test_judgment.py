from unittest import TestCase
from kant import Judgment


class TestJudgment(TestCase):
    def test_make(self):
        c = Judgment()
        self.assertTrue(isinstance(c, Judgment))