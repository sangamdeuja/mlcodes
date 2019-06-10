def function(n,x):

    if n<5:
        x=5
    if n==8:
        print("course passed")
    elif n<5 or x==5:
        function(n+1,5)
    else:
        while True:
            print(n)
            n=n+1

function(6,0)

