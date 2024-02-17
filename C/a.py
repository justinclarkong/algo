#!/usr/bin/env python3
t = int(input())
for i in range(t):
    c = [s[:1] for s in input().split(" ")]
    p = input().split(" ")
    n = int(input())
    for j in range(n):
        total = sum([int(p[c.index(char)]) for char in list(input())])
        print("NEGATIVE" if total < 0 else "POSITIVE" if total > 0 else "NEUTRAL")
