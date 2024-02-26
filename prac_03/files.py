# Question 1
name = input("Enter your name: ")
file = open("name.txt", 'w')
file.write(name)
file.close()

# Question 2
file = open("name.txt", 'r')
name_read = file.read()
print(f"Your name is {name_read}")
file.close()

# Question 3
with open("numbers.txt", 'r') as number_file:
    number_1 = int(number_file.readline())
    number_2 = int(number_file.readline())
print(number_1 + number_2)

# Question 4
with open("numbers.txt", 'r') as number_file:
    for line in number_file:
        print(line.strip())