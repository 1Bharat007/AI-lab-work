import random

def create_chromosome():
    return [random.randint(0, 1) for _ in range(5)]

def decode(chromosome):
    return int("".join(map(str, chromosome)), 2)

def fitness(chromosome):
    x = decode(chromosome)
    return x * x

population = [create_chromosome() for _ in range(10)]

for generation in range(20):
    population.sort(key=fitness, reverse=True)

    if fitness(population[0]) == 961:
        break

    new_population = population[:2]

    while len(new_population) < 10:
        parent1 = random.choice(population[:5])
        parent2 = random.choice(population[:5])

        point = random.randint(1, 4)

        child = parent1[:point] + parent2[point:]

        if random.random() < 0.1:
            index = random.randint(0, 4)
            child[index] = 1 - child[index]

        new_population.append(child)

    population = new_population

best = max(population, key=fitness)
print("Best chromosome:", best)
print("Value:", decode(best))
print("Fitness:", fitness(best))