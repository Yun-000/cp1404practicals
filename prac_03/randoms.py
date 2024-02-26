import random

print(random.randint(5, 20))
# line 1 Answer: A random integer between 5 and 20 (inclusive).
# Smallest number: 5
# Biggest number: 20

print(random.randrange(3, 10, 2))
# line 2 Answer: A random odd integer between 3 and 10 (basically 3, 5, 7, 9).
# Smallest number: 3
# Biggest number: 9
# Cannot produce a 4

print(random.uniform(2.5, 5.5))
# line 3 Answer: A random float between 2.5 and 5.5 (inclusive).
# Possible smallest number: 2.5
# Possible biggest number: 5.5

print(random.uniform(0, 100))