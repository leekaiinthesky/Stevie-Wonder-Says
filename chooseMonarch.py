import random

with open('listOfMonarchs.txt') as f:
    monarchs = set(f.read().splitlines())

with open('featuredMonarchs.txt') as f:
    featured = set(f.read().splitlines())

# put a monarch that isn't in 'featuredMonarchs.txt' into 'chosenMonarch.txt'

with open('chosenMonarch.txt', 'w') as f:
    f.write(random.choice(list(monarchs - featured)))
