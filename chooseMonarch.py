import random

with open('listOfMonarchs.txt') as f:
    monarchs = set(f.read().splitlines())

with open('featuredMonarchs.txt') as f:
    featured = set(f.read().splitlines())

print len(monarchs)
print len(featured)

# print random.choice(list(monarchs - featured))
# Richard I of England