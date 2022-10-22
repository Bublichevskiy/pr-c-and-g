N = int(input())
A = [int(s) for s in input().split()]
P = int(input())
A.pop(P-1)
(Q, K) = [int(s) for s in input().split()]
A.insert(K, Q - 1)
print(" ".join([str(i) for i in A ]))