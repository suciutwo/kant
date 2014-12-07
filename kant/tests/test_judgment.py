from unittest import TestCase
from kant import Concept, Judgment


class TestJudgment(TestCase):
    def test_make(self):
        """ Creating a judgment """
        c = Judgment(Concept("subject"), Concept("predicate"))
        self.assertTrue(isinstance(c, Judgment))
        self.assertTrue(c.predicate.name == "predicate")

    def test_straight_line(self):
        """ pp145 """
        straight = Concept("straight line")
        shortest = Concept("shortest possible")
        j = Judgment(straight, shortest)
        self.assertTrue(j.is_synthetic())

    def test_bodies(self):
        """ pp130 """
        space = Concept("space", [Concept("extended")])
        all_bodies = Concept("all bodies", [space])
        extended = Concept("extended")
        j = Judgment(all_bodies, extended)
        self.assertTrue(j.is_analytic())
        heavy = Concept("heavy")
        j = Judgment(all_bodies, heavy)
        self.assertTrue(j.is_synthetic())

    def test_science(self):
        """ pp145 """
        matter = Concept("matter", [Concept("presence")])
        conserved = Concept("persistence")
        all_matter_is_conserved = Judgment(matter, conserved)
        self.assertTrue(matter.contains(Concept("presence")))
        self.assertTrue(all_matter_is_conserved.is_synthetic())

