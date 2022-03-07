from math import floor
import random 
from .chromosome import *

class Population:
    def __init__(self, target, mutation_rate, popmax, gene_set, num_genes):
        self.population = []
        self.matingPool = []
        self.generations = 0
        self.finished = False

        self.target = target
        self.mutation_rate = mutation_rate
        self.perfectScore = 1
        self.best = None
        
        # initialize population randomly
        for _ in range(popmax):
            self.population.append(Chromosome(gene_set, num_genes))


    def calcFitness(self):
        ## Calculate fitness of all chromosomes of generation
        for i in range(len(self.population)):
            self.population[i].calcFitness(self.target)

    
    def naturalSelection(self):
        ## Generate a mating pool

        # Clear the ArrayList
        self.matingPool = []

        ################ Find Fittest ################
        maxFitness = 0
        for i in range(len(self.population)):
            if (self.population[i].fitness > maxFitness):
                maxFitness = self.population[i].fitness
        
        ################ Construt Mating Pool #################
        # Based on fitness, each member will get added to the mating pool a certain number of times
        # a higher fitness = more entries to mating pool = more likely to be picked as a parent
        # a lower fitness = fewer entries to mating pool = less likely to be picked as a parent
        multiplier = 100
        for i in range(len(self.population)):
            fitness = self.population[i].fitness / maxFitness
            assert (fitness >=0 and fitness <=1)    #check bounds
            n = floor(fitness * multiplier)
            for _ in range(n):
                self.matingPool.append(self.population[i])


    def generate(self): 
        ## Create a new generation

        for i in range(len(self.population)):

            # select two partners from pool
            partnerA = random.choice(self.matingPool)
            partnerB = random.choice(self.matingPool)

            # reproduce
            child = partnerA.crossover(partnerB)
            child.mutate(self.mutation_rate)
            self.population[i] = child
        
        self.generations +=1

    def getBest(self):
        # get fittest Chromosome
        return self.best

    
    def evaluate(self):
        # compute most fit candidate
        max = 0
        index = 0

        for i in range(len(self.population)):
            if (self.population[i].fitness > max):
                index = i
                max = self.population[i].fitness

        self.best = self.population[index]
        if max == self.perfectScore:
            self.finished = True


    def isFinished(self):
        return self.finished
    

    def getAvgFitness(self):
        total = 0
        for i in range(len(self.population)):
            total += self.population[i].fitness
        return total/len(self.population)
    