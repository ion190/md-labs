def powerset(input_set):
    if len(input_set) == 0:
        return [[]]  # The powerset of an empty set is a set containing the empty set

    element = input_set.pop()
    subsets = powerset(input_set)
    new_subsets = [subset + [element] for subset in subsets]

    return subsets + new_subsets

# Input set
input_set = eval(input())

# Convert the set to a list (sets are not indexable)
input_list = list(input_set)

# Calculate the powerset
result = powerset(input_list)

print(result)


# input_set = eval(input("Input = "))
# output = [[]]

# for l in range(1, len(input_set)):
    
#     for i in range(0, len(input_set)):
#         subset = []
#         for l_subset in range(0, l):
#             subset.append(input_set[i])
#         output.append(subset)
# output.append(input_set)
# print(output)

        
        
        
        
        

