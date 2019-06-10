def solution(a):
    a.sort()
    for i in range(0,len(a)-2):
        if a[i]+a[i+1]>a[i+2]:
            return 1

    return 0

a=[]
solution(a)
