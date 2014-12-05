from unittest import TestCase
from kant import Concept, Judgment


class TestJudgment(TestCase):
    def test_make(self):
        c = Judgment(Concept("subject"), Concept("predicate"))
        self.assertTrue(isinstance(c, Judgment))

    def test_straight_line(self):
        """pp145"""
        straight = Concept("straight line")
        shortest = Concept("shortest possible")
        j = Judgment(straight, shortest)
        self.assertTrue(j.is_synthetic())