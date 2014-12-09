from unittest import TestCase
from kant import Concept, Judgment


class TestJudgment(TestCase):
    def test_make(self):
        """ Creating a judgment """
        c = Judgment(Concept("subject", False), Concept("predicate", False))
        self.assertTrue(isinstance(c, Judgment))
        self.assertTrue(c.predicate.name == "predicate")

    def test_straight_line(self):
        """ pp145 """
        straight = Concept("straight line", "True")
        shortest = Concept("shortest possible", "True")
        j = Judgment(straight, shortest)
        self.assertTrue(j.is_synthetic())

    def test_bodies(self):
        """ pp130 """
        space = Concept("space", False, [Concept("extended", True)])
        all_bodies = Concept("all bodies", False, [space])
        extended = Concept("extended", True)
        j = Judgment(all_bodies, extended)
        self.assertTrue(j.is_analytic())
        heavy = Concept("heavy", True)
        j = Judgment(all_bodies, heavy)
        self.assertTrue(j.is_synthetic())

    def test_science(self):
        """ pp145 """
        matter = Concept("matter", True, [Concept("presence", True)])
        conserved = Concept("persistence", True)
        all_matter_is_conserved = Judgment(matter, conserved)
        self.assertTrue(matter.contains(Concept("presence", True)))
        self.assertTrue(all_matter_is_conserved.is_synthetic())


    def test_purity(self):
        c = Concept("one", False)
        c2 = Concept("two", False)
        j = Judgment(c, c2)
        self.assertTrue(j.is_pure())
        c.analytic_facets = [Concept("three", True)]
        self.assertFalse(j.is_pure())
