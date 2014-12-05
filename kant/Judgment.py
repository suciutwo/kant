from concept import Concept

class Judgment():

    def __init__(self):
        self.subject = Concept()
        self.predicate = Concept()

    def is_analytic(self):
        return not self.is_synthetic()

    def is_synthetic(self):
        return self.subject.contains(self.predicate)



