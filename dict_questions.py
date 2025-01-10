# dict programming questions
# 1.Write a program to merge two dictionaries into one.
# dict1 = {
#     "name": "John",
#     "age": 30
# }
# dict2 = {
#     "city": "New York",
#     "country": "USA"
# }
# dict1.update(dict2)
# print(dict1)

# 2.Create a Python program to find the key of the maximum value in a dictionary.
# max_dict = {
#         "a": 1,
#         "b": 2,
#         "c": 3,
#         "d": 4,
#         "e": 5,
#         "f": 6
#     }
# print(max(max_dict))

# 3.Write a program to invert a dictionary (swap keys and values).
# uninverted_dict = {
#     "a": "apple",
#     "b": "banana",
#     "c": "cherry"
# }
# print({v: k for k, v in uninverted_dict.items()})

# 4.Create a program to count the frequency of characters in a given string using a dictionary.
# freq_string = "hello"
# freq_dict = {}
# for char in freq_string:
#     if char in freq_dict:
#         freq_dict[char] += 1
#     else:
#         freq_dict[char] = 1
# print(freq_dict)

# 5.Write a Python program to remove a specific key from a dictionary.
# remove_dict = {
#     "name": "John",
#     "age": 30,
#     "city": "New York"
# }
# remove_dict.pop("age")
# print(remove_dict)

# 6.Create a program to check if a dictionary is empty.
# empty_dict = {}
# not_empty_dict = {
#     "name": "John"
# }
# def check_dict(dict1):
#     if len(dict1) == 0:
#         return "Dictionary is empty"
#     else:
#         return "Dictionary is not empty"

# print(check_dict(empty_dict))
# print(check_dict(not_empty_dict))

# 7.Write a program to sort a dictionary by its values in descending order.
# unsorted_dict = {
#     "a": 3,
#     "b": 1,
#     "c": 2
# }
# sorted_dict = dict(sorted(unsorted_dict.items(), key= lambda x: x[1],reverse=True))
# print(sorted_dict)

# 8.Write a Python program to update a dictionary with another dictionary's keys and values.
# dict1 = {'a': 1, 'b': 2}
# dict2 = {'c': 3, 'd': 4}
# dict1.update(dict2)
# print(dict1)

# 9.Write a program to check if a key exists in a dictionary.
# exists_dict = {
#     "name": "John",
#     "age": 30
# }

# key_to_check = "name"
# if key_to_check in exists_dict:
#     print("Key exists")

# print(exists_dict.get("name"))