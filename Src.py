## my code solves the equation. 

# solution: 


import itertools

arr = [4, 9, 1, 32, 13]

if len(arr) > 1:
    min_diff = abs(arr[0] - arr[1])
else:
    min_diff = 0

for n1, n2 in itertools.combinations(arr, 2): # Get the combinations of numbers
    diff = abs(n1-n2) # Find the absolute difference of each combination
    if min_diff > diff:
        min_diff = diff # Replace incase a least differnce found

print(min_diff)
