import random
# returns a list with a random selection from the given sequence
mylist = ["Eammon", "Edward", "Twitter", "Gonze"]

print(random.choices(mylist, weights=[10, 1, 2, 3], k=14))
