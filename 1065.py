def solution():
    N = int(input())
    X = [str(x) for x in range(1,N+1)]
    i = 0
    Solve = set()

    for x in X:

        for j in range(1,len(x)):
            Solve.add(int(x[-j]) - int(x[-j-1]))
        
        if len(Solve) == 1 or len(x) == 1:
            i += 1
        Solve = set()

    return(i)
print(solution())