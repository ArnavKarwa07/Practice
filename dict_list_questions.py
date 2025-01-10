# combination of list and dict
# 1.Create a Python program to filter a list of dictionaries based on a specific key's value.
# list_to_be_filtered = [{'key1': 'value1'}, {'key2': 'value2'}, {'key3': 'value1'}, {'key4': 'value2'}]
# filter_value = 'value1'
# filtered_list = []
# for dictionary in list_to_be_filtered:
#     for key, value in dictionary.items():
#         if value == filter_value:
#             filtered_list.append(dictionary)
#             break
# print(filtered_list)

# 2.Write a program to create a dictionary where keys are elements from a list and values are their squares.
# numbers = [1, 2, 3, 4, 5]
# squares = {}
# for number in numbers:
#     squares[number] = number**2
# print(squares)

# 3.Create a Python program to group a list of numbers into even and odd using a dictionary.
# even_odd_list = [x for x in range(10)]
# even_odd_dict = {'even': [], 'odd': []}
# for number in even_odd_list:
#     if number % 2 == 0:
#         even_odd_dict['even'].append(number)
#     else:
#         even_odd_dict['odd'].append(number)
# print(even_odd_dict)

# 4.Create a program to find the dictionary with the highest value for a specific key in a list of dictionaries.
# list_of_dictionaries = [{'key1': 1}, {'key2': 2}, {'key1': 3}, {'key2': 4}]
# key_to_find = 'key1'
# max_value = 0
# max_dict = {}

# for dictionary in list_of_dictionaries:
#     if key_to_find in dictionary:
#         value = dictionary[key_to_find]
#         if value > max_value:
#             max_value = value
#             max_dict = dictionary
# print(max_dict)

# 5.Write a Python program to create a dictionary from a list where keys are indices and values are elements.
# alphabets = ['a', 'b', 'c', 'd', 'e']
# index_dict = {}
# for alphabet in alphabets:
#     index_dict[alphabets.index(alphabet)] = alphabet
# print(index_dict)

# 6.Create a program to sort a list of dictionaries by a specific key.
# data = [
#     {'name': 'John', 'age': 25},
#     {'name': 'Alice', 'age': 30},
#     {'name': 'Bob', 'age': 20},
#     {'name': 'Charlie', 'age': 28}
# ]
# sorted_data = sorted(data, key=lambda x: x['age'])
# for item in sorted_data:
#     print(item)

# 7.Create a Python program to update the value of a dictionary if its key exists in a given list.
# def update_dictionary(dictionary, key_list, new_value):
#     for key in key_list:
#         if key in dictionary:
#             dictionary[key] = new_value
#     return dictionary

# my_dict = {'a': 1, 'b': 2, 'c': 3}
# my_list = ['a', 'd']
# new_value = 10

# update_dictionary(my_dict, my_list, new_value)
# print(my_dict)
