#!/usr/bin/env python3
t = int(input())
for _ in range(t):
    n = int(input())
    s = [int(s) for s in input().split()]
    t = []
    for i in range(len(s)):
        c = [j for j in s[i+1:] if j > s[i]]
        t.append(str(s[i+1:].index(min(c))+i+2) if c else str(i+1))

    print(" ".join(t))
