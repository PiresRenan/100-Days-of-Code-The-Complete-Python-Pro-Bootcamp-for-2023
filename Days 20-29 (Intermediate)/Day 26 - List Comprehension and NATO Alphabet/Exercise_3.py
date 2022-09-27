with open("file1.txt", mode="r") as file_1:
    data_file1 = file_1.readlines()
with open("file2.txt", mode="r") as file_2:
    data_file2 = file_2.readlines()

result = [int(num) for num in data_file1 if num in data_file2]
# Write your code above 👆

print(result)

#  Dictionary Comprehension 1
# Instructions
# Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers, each number on a new line.
# You are going to create a list called result which contains the numbers that are common in both files.
# e.g. if file1.txt contained:
# 1
# 2
# 3
# and file2.txt contained:
# 2
# 3
# 4
# result = [2, 3]
# IMPORTANT: The result should be a list that contains Integers, not Strings. Try to use List Comprehension instead of a Loop.
