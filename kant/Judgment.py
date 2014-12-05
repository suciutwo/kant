from concept import Concept

class Judgment():

    def __init__(self, subject, predicate):
        if not isinstance(subject, Concept):
            raise TypeError("subject must be a concept")
        self.subject = subject
        if not isinstance(predicate, Concept):
            raise TypeError("predicate must be a concept")
        self.predicate = predicate

    def is_analytic(self):
        return not self.is_synthetic()

    def is_synthetic(self):
        return self.subject.contains(self.predicate)



