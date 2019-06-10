import numpy as np

def solution(A):
    myarray = np.array(A)
    abs_array=np.absolute(myarray)
    unique_array = set(abs_array)
    return len(unique_array)

A = [-5, -3, -1, 0, 3, 6,-2,7,-7]
print(solution(A))
