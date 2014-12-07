class Concept(object):

    def __init__(self, name, facets=None):
        """
        :param name: String
        :param facets: [Concept]
        :return:
        """
        self._name = None
        self.name = name
        self._analytic_facets = None
        self.analytic_facets = facets

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
        if not self.analytic_facets:
            return False
        for concept in self.analytic_facets:
            if predicate.equals(concept):
                return True
        return False