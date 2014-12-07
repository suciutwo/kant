from concept import Concept


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



