#!/usr/bin/env python3
t = int(input())
for _ in range(t):
    S = []
    F = []
    n = int(input())

    for _ in range(n):
        intervals = input().split(" - ")

        hhmmss = intervals[0].split(":")
        S.append((int(hhmmss[0]) * 60*60) + (int(hhmmss[1]) * 60) + int(hhmmss[2]))

        hhmmss = intervals[1].split(":")
        F.append((int(hhmmss[0]) * 60*60) + (int(hhmmss[1]) * 60) + int(hhmmss[2]))

    S.sort()
    F.sort()

    acts = [F[0]]
    for k, v in enumerate(F):
        if S[k] > acts[-1]:
            acts += [v]

    print(len(acts))
