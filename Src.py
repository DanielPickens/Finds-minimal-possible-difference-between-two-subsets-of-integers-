## my code solves the equation. 

# solution: 


import itertools

arr = [4, 9, 1, 32, 13]

if len(arr) > 1:
    min_diff = abs(arr[0] - arr[1])
else:
    min_diff = 0

for name_given_1, name_given_2 in itertools.combinations(arr, 2): # Get the combinations of numbers
    diff = abs(nanem_given_1-name_given_2) # Find the absolute difference of each combination
    if min_diff > diff:
        min_diff = diff # Replace incase a least differnce found

print(min_diff)
