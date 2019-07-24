"""
Given a list of items where each item has a weight (integer value),
select a random item from the list based on that weight
fruits = [apple, orange, lemon]
intervals = [4, 6, 7]
"""
from random import random

population = ["apple", "orange", "lemon"]
weights = [4, 6, 7]

def random_select(container, weights):
    # total sum of all weights
    total_weights = float(sum(weights))
    # relative weight
    rel_weight = [w/total_weights for w in weights]
    # cal the prob with rel weights
    prob = [sum(rel_weight[:i +1]) for i in range(len(rel_weight))]
    slot = random()
    for (i, element) in enumerate(container):
        if slot <= prob[i]:
            break
    return element

if __name__ == "__main__":
    print(random_select(population, weights))



