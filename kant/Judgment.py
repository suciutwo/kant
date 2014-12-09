from concept import Concept

def _subconcepts_are_pure(concept):
    if not concept.is_from_experience:
        return False
    for subconcept in concept.analytic_facets:
        if not _subconcepts_are_pure(subconcept):
            return False
    return True


class Judgment(object):

    def __init__(self, subject, predicate):
        self._subject = None
        self.subject = subject
        self._predicate = None
        self.predicate = predicate

    @property
    def predicate(self):
        return self._predicate

    @predicate.setter
    def predicate(self, predicate):
        if not isinstance(predicate, Concept):
            raise TypeError("predicate must be a concept")
        self._predicate = predicate

    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, subject):
        if not isinstance(subject, Concept):
            raise TypeError("subject must be a concept")
        self._subject = subject

    @subject.deleter
    def subject(self):
        del self._subject

    def is_analytic(self):
        return not self.is_synthetic()

    def is_synthetic(self):
        return not self.subject.contains(self.predicate)


    def is_pure(self):
        if _subconcepts_are_pure(self.subject):
            if _subconcepts_are_pure(self.predicate):
                return True
        return False

    def is_apriori(self):
        """pp136"""
        return

    def is_empirical(self):
        """pp136"""
        return not self.is_apriori()

