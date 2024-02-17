#!/usr/bin/env python3
from collections import deque

t = int(input())
for i in range(t):
    s, n = [int(i) for i in input().split()]
    m = deque(input().split())
    for j in range(s):
        p = deque(input().split())
        for k in range(n):
            m.rotate()
            if m == p:
                print(j+1)
