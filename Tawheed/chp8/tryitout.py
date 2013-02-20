# Question1
table = int(raw_input("Which multiplication table would you like: "))
for i in range(1,11):
	print table, " * ", i, " = ", i*table

# Question
table = int(raw_input("Which multiplication table would you like: "))
i = 1
while i <= 10:
	print table, " * ", i, " = ", i*table
	i = i +1

# Question 3a
high = int(raw_input("How high do you want the number: "))
multiplication = int(raw_input("What multiplication table would you like: "))
for i in range(1,high+1):
	print i, " * ",multiplication, " = ",  multiplication * i


# Question a
high = int(raw_input("How high do you want the number: "))
multiplication = int(raw_input("What multiplication table would you like: "))
i = 1
while i <= high:
	print i, " * ", multiplication, " = ",  multiplication * i
	i = i+1
