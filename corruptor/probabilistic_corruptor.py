"""probabilistic_corruptor.py"""
from corruptor import BasicCorruptor
from random import choices

class ProbabilisticCorruptor(BasicCorruptor):
    """ProbabilisticCorruptor definition"""

    def __init__(self, probabilities):
        super().__init__()

        if sum(probabilities.values()) not in [0.99, 1.00, 1.01]:
            raise Exception('Probabilities must add up to one.')
        
        corruptions = sorted([c for c in probabilities.keys() if c in self.corruptions.keys()])
        if len(corruptions) != len(probabilities):
            raise Exception('Probability for unsupported corruptor type found, ' +
                            'please double check names in probability dictionary.')

        self.population = [self.corruptions[c] for c in corruptions]
        self.weights = [probabilities[c] for c in corruptions]

    def corrupt(self, string):
        corruption = choices(self.population, self.weights, k=1)[0]
        if corruption is None:
            return string

        return corruption.corrupt_value(string)