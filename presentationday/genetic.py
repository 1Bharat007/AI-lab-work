import random

POPULATION_SIZE = 6
GENERATIONS = 20
MUTATION_RATE = 0.1


# Convert binary chromosome to decimal
def decode(chromosome):
    return int(chromosome, 2)


# Fitness function: maximize x^2
def fitness(chromosome):
    x = decode(chromosome)
    return x * x


# Create a random 5-bit chromosome
def create_chromosome():
    return ''.join(random.choice("01") for _ in range(5))


# Create initial population
population = [create_chromosome() for _ in range(POPULATION_SIZE)]


for generation in range(GENERATIONS):

    # Selection: keep the best half
    population.sort(key=fitness, reverse=True)
    parents = population[:POPULATION_SIZE // 2]

    print("Generation:", generation + 1,
          "Best:", parents[0],
          "Fitness:", fitness(parents[0]))

    # Keep the best solution unchanged (elitism)
    new_population = [parents[0]]

    # Crossover and mutation
    while len(new_population) < POPULATION_SIZE:

        p1 = random.choice(parents)
        p2 = random.choice(parents)

        # Single-point crossover
        point = random.randint(1, 4)
        child1 = p1[:point] + p2[point:]
        child2 = p2[:point] + p1[point:]

        # Mutation: randomly flip bits
        for child in (child1, child2):
            bits = list(child)

            for i in range(5):
                if random.random() < MUTATION_RATE:
                    bits[i] = '1' if bits[i] == '0' else '0'

            new_population.append(''.join(bits))

            if len(new_population) == POPULATION_SIZE:
                break

    population = new_population


# Display the final best solution
best = max(population, key=fitness)

print("\nBest chromosome:", best)
print("Best x:", decode(best))
print("Maximum fitness:", fitness(best))