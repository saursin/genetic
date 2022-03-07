#!/bin/python3
from genetic import *
import string

# Target Phrase
Target = "How To Train a Dragon"

# Set of all letters to use
gene_set = string.ascii_letters+" "

# max population per generation
popmax = 2000

# Rate of mutation
mutation_rate = 0.01

# Create initial population
population =  Population(Target, mutation_rate, popmax, gene_set, len(Target))

best = "_"*len(Target)
while not population.isFinished():    
    
    # calculate fitness of all candidates
    population.calcFitness()

    # Get the Best-fit Candidate
    population.evaluate()
    best = population.getBest()

    print("Generation: ", population.generations, " \tAverage Fitness: ", str(round(population.getAvgFitness(), 4)).zfill(6), " \tBest Candidate: ", best.getSignature(), " [Fitness:", round(best.fitness, 4), "]")
    
    # Generate mating pool through natural selection (survival of the fittest!)
    population.naturalSelection()

    # Get new generation by reproducing candidates of mating pool
    population.generate()
  

print(">> Done! (in ", population.generations,"generations of a population of",len(population.population),"candidates with a mutation rate of",population.mutation_rate*100,"%)")
