from unittest import TestCase
from kant import Concept


class TestConcept(TestCase):
    def test_make(self):
        """ Creating a concept """
        c = Concept("test concept", False, [Concept("sub concept", False)])
        self.assertTrue(isinstance(c, Concept))
        self.assertTrue(c.contains(Concept("sub concept", False)))