"""probabilistic_corruptor.py"""
from corruptor import Corruptor
from random import choices

class ProbabilisticCorruptor(Corruptor):
    """ProbabilisticCorruptor definition"""

    def __init__(self, probabilities):
        super().__init__()

        if sum(probabilities.values()) != 1:
            raise Exception('Probabilities must add up to one.')
        
        corruptors = sorted([c for c in probabilities.keys() if c in self.corruptors.keys()])
        if len(corruptors) != len(probabilities):
            raise Exception('Probability for unsupported corruptor found, ' +
                            'please double check names in probability dictionary.')

        self.population = [self.corruptors[c] for c in corruptors]
        self.weights = [probabilities[c] for c in corruptors]

    def apply(self, string):
        corruptor = choices(self.population, self.weights, k=1)[0]
        return corruptor.corrupt_value(string)