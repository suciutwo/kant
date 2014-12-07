from unittest import TestCase
from kant import Concept


class TestConcept(TestCase):
    def test_make(self):
        """ Creating a concept """
        c = Concept("test concept", [Concept("sub concept")])
        self.assertTrue(isinstance(c, Concept))
        self.assertTrue(c.contains(Concept("sub concept")))