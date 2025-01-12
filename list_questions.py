# list programming questions
# 1.Write a program to find the second-largest element in a list of integers.
# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# numbers.sort
# print(numbers[-2])

# 2.Create a list of numbers from 1 to 20 and filter out even numbers using list comprehension.
# numbers = [i for i in range(1, 21) if i % 2 != 0]
# print(numbers)

# 3.Write a program to reverse a list without using the reverse() method.
# list_to_be_reversed = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list_to_be_reversed[::-1])

# 4.Merge two lists into a single sorted list without duplicates.
# list1 = [3,5,2,6,7,8,9]
# list2 = [1,7,3,8,9,4,0]
# merged_list = list1 + list2
# print(sorted(set(merged_list)))

# 5.Write a program to find all the unique elements in a list.
# not_unique_list = [1,1,2,2,3,4,5,6,7,8,8,9,0,0]
# unique_list = set(not_unique_list)
# print(unique_list)

# 6.Implement a program to rotate a list by n positions to the right.
# list_to_be_rotated = [1,2,3,4,5,6,7,8,9,0]
# def  rotate_list(list1, n):
#     return list1[-n:] + list1[:-n]
# print(rotate_list(list_to_be_rotated, 3))

# 7.Write a program to find the frequency of each element in a list.
# freq_list = [1,1,1,2,2,3,4,5,5,6,6,7]
# def frequency(flist, n):
#     return flist.count(n)
# print(frequency(freq_list, 2))

# 8.Create a list of tuples where each tuple contains a number and its square for numbers from 1 to 10.
# squares = [(i, i**2) for i in range(1, 11)]
# print(squares)

# 9.Write a program to find the maximum and minimum element in a list without using the built-in max() and min() functions.
# max_min_list = [1,2,3,4,5,6,7,8,9,0]
# def find_max(numbers):
#     for i in range(len(numbers)-1):
#         max = numbers[i]
#         if numbers[i+1] > max:
#             max = numbers[i+1]
#         i += 1
#     return max

# def find_min(numbers):
#     for i in range(len(numbers)-1):
#         min = numbers[i]
#         if numbers[i+1] < min:
#             min = numbers[i+1]
#         i += 1
#     return min
# print("Maximum:", find_max(max_min_list))
# print("Minimum:", find_min(max_min_list))
