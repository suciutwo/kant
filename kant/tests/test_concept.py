from unittest import TestCase
from kant import Concept


class TestConcept(TestCase):
    def test_make(self):
        c = Concept("test concept")
        self.assertTrue(isinstance(c, Concept))