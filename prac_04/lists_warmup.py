numbers = [3, 1, 4, 1, 5, 9, 2]
# 3
print(numbers[0])
# 2
print(numbers[-1])
# 1
print(numbers[3])
# [3, 1, 4, 1, 5, 9]
print(numbers[:-1])
# [1]
print(numbers[3:4])
# True
print(5 in numbers)
# False
print(7 in numbers)
# False
print("3" in numbers)
# [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
print(numbers + [6, 5, 3])

# Question 1
numbers[0] = 'ten'

# Question 2
numbers[-1] = 1

# Question 3
print(numbers[2:])

# Question 4
print(9 in numbers)