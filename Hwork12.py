# დავალება 1

# def duplicates(a):
#     unique_values = set()
#     delete = []

#     for key, value in a.items():
#         if value not in unique_values:
#             unique_values.add(value)
#         else:
#             delete.append(key)
#     for key in delete:
#         del a[key]
#     return a

# dict = {'a': 1, 'b': 2, 'c': 2, 'd': 3}
# print(duplicates(dict))

# ---------------------------------------------------


# # დავალება 2

# def is_dict_empty(input_dict):
#     if len(input_dict) == 0:
#         return "The dictionary is empty."
#     else:
#         return "The dictionary is not empty."
# empty_dict = {}
# dict = {'Something': '1'}

# empty = is_dict_empty(empty_dict)
# notempty = is_dict_empty(dict)

# print(empty)
# print(notempty)

# ---------------------------------------------------


# დავალება 3

# def Count(input_string):
#     char_dict = {}
#     for charact in input_string:
#         if charact in char_dict:
#             char_dict[charact] += 1
#         else:
#             char_dict[charact] = 1
#     return char_dict
# result = Count("racoon")
# print(result)