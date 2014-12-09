class Concept(object):

    def __init__(self, name, is_from_experience, facets=None):
        """
        :param name: String
        :param facets: [Concept]
        :return:
        """
        self._name = None
        self.name = name
        self._analytic_facets = None
        self.analytic_facets = facets
        self.is_from_experience = is_from_experience

    def __eq__(self, other):
        if not isinstance(other, Concept):
            return False
        return self.name == other.name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @name.deleter
    def name(self):
        del self._name

    def contains(self, predicate):
        if self == predicate:
            return True
        if self.analytic_facets:
            for concept in self.analytic_facets:
                if concept.contains(predicate):
                    return True
        return False

    def is_pure(self):
        if self.is_from_experience:
            return False
        if self.analytic_facets:
            for concept in self.analytic_facets:
                if not concept.is_pure():
                    return False
        return True