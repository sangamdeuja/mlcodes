def solution(A,K):
    for i in range(0,K):
        a=A.pop()
        A.insert(0,a)
        print(A)

solution([2,3,4,5,6,7],5)