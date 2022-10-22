N = int(input())
A = [int(s) for s in input().split()]
P = int(input())
A.insert(0, A.pop(P-1))
print(" ".join([str(i) for i in A ]))