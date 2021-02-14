## my code solves the equation. 

          
         ######### best: solution all around: 
          
          def findMinReq(arr, i, sumCalculated, 
        sumTotal):
  if (i == 0):
    return abs((sumTotal - sumCalculated) -
          sumCalculated)
  return min(findMinReq(arr, i - 1, 
             sumCalculated+arr[i - 1], 
             sumTotal),
        findMinReq(arr, i - 1, 
             sumCalculated, sumTotal))

def findMin(arr, nbdy):
  sumTotal = 0
  for i in range(nbdy):
    sumTotal += arr[i]
 
  return findMinReq(arr, nbdy, 
           0, sumTotal)
            
if __name__ == "__main__":
 
  arr = [3, 7, 5, 1]
  nbdy = len(arr)
  print("The minimum difference " +
     "between two sets is ", 
      findMin(arr, nbdy))















import itertools

arr = [3,7,2,5]

if len(arr) > 1:
    min_diff = abs(arr[0] - arr[1])
else:
    min_diff = 0

for name_given_1, name_given_2 in itertools.combinations(arr, 2): # Get the combinations of numbers
    diff = abs(nanem_given_1-name_given_2) # Find the absolute difference of each combination
    if min_diff > diff:
        min_diff = diff # Replace incase a least differnce found

print(min_diff)




Solution 2: 

import itertools as it

def min_diff_sets(data):
    """
        Parameters:
        - `data`: input list.
        Return:
        - min diff between sum of numbers in two sets
    """

    if len(data) == 1:
        return data[0]
    s = sum(data)
    # `a` is list of all possible combinations of all possible lengths (from 1
    # to len(data) )
    a = []
    for i in range(1, len(data)):
        a.extend(list(it.combinations(data, i)))
    # `b` is list of all possible pairs (combinations) of all elements from `a`
    b = it.combinations(a, 2)
    # `c` is going to be final correct list of combinations.
    # Let's apply 2 filters:
    # 1. leave only pairs where: sum of all elements == sum(data)
    # 2. leave only pairs where: flat list from pairs == data
    c = filter(lambda x: sum(x[0])+sum(x[1])==s, b)
    c = filter(lambda x: sorted([i for sub in x for i in sub])==sorted(data), c)
    # `res` = [min_diff_between_sum_of_numbers_in_two_sets,
    #           ((set_1), (set_2))
    #         ]
    res = sorted([(abs(sum(i[0]) - sum(i[1])), i) for i in c],
            key=lambda x: x[0])
    return min([i[0] for i in res])

if __name__ == '__main__':
    assert min_diff_sets([10, 10]) == 0, "1st example"
    assert min_diff_sets([10]) == 10, "2nd example"
    assert min_diff_sets([5, 8, 13, 27, 14]) == 3, "3rd example"
    assert min_diff_sets([5, 5, 6, 5]) == 1, "4th example"
