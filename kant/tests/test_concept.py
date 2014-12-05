from unittest import TestCase
from kant import Concept


class TestConcept(TestCase):
    def test_make(self):
        c = Concept()
        self.assertTrue(isinstance(c, Concept))