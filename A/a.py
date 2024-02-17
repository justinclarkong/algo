#!/usr/bin/env python3
import sys

t = int(input())
n = 0

while n < t:
    n += 1
    r, c = input().split(" ")
    r, c = int(r), int(c)
    grid = [list(l) for l in sys.stdin.read((r * c) + r).strip("\n").split("\n")]
    h = [x for x in grid if 'X' in x]
    v = [x for x in [[x[i] for x in h] for i in range(c)] if 'X' in x]
    print(min(len(h), len(v)))
