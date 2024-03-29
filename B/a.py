#!/usr/bin/env python3
t = int(input())
for i in range(t):
    n = int(input())
    planets = {"Mercury":0,"Venus":0,"Earth":0,"Mars":0,"Jupiter":0,"Saturn":0,"Uranus":0,"Neptune":0,"Pluto":0}
    for j in range(n):
        p = input().split()
        for k in range(2, int(p[0])+1):
            planets[p[k]] += 1

    for k, v in sorted(planets.items(), key=lambda x: (-x[1], x[0])):
        print(f"{k} {v}")
