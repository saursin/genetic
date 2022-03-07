from math import floor
import random

class Chromosome:
    def __init__(self, gene_set, num):
        self.gene_set = gene_set
        self.genes = []
        self.fitness = 0

        # create genes
        for _ in range(num):
            self.genes.append(random.choice(gene_set))


    def getSignature(self):
        ## Get gene signature as string
        if type(self.gene_set) == str:
            return "".join(self.genes)


    def calcFitness(self, target):
        # Calculate fitness of gene
        score = 0
        for i in range(len(self.genes)):
            if(self.genes[i] == target[i]):
                score +=1
        self.fitness = score / len(target)


    def crossover(self, partner):
        child = Chromosome(self.gene_set, len(self.genes))

        # pick random splitpoint
        splitpt = floor(random.randrange(len(self.genes)))
        for i in range(len(self.genes)):
            if i > splitpt:
                child.genes[i] = self.genes[i]
            else:
                child.genes[i] = partner.genes[i]
        
        return child

    def mutate(self, mutation_rate):
        for i in range(len(self.genes)):
            if(random.random() < mutation_rate):
                self.genes[i] = random.choice(self.gene_set)