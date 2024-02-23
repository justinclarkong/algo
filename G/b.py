#!/usr/bin/env python3
def select_times(intervals):
    intervals.sort(key=lambda x: x[1])
    count = 0
    end = 0
    answers = 0
    for interval in intervals:
        if end < interval[0]:
            end = interval[1]
            count += 1
            answers += 1
    return answers

def main():
    test_cases = int(input())
    test_cases_answers = []
    for _ in range(test_cases):
        n = int(input())
        intervals = []
        for i in range(n):
            time_ranges = parse_time(input())
            intervals.append(time_ranges)
        no_ans = select_times(intervals)
        test_cases_answers.append(no_ans)
    
    for ans in test_cases_answers:
        print(ans)

def parse_time(t):
    t = t.split(" - ")
    sh, sm, ss = t[0].split(":")
    fh, fm, fs = t[1].split(":")
    ints = float(sh) + (float(sm) * 1/60) + (float(ss) * 1/3600)
    intf = float(fh) + (float(fm) * 1/60) + (float(fs) * 1/3600)
    interval = (ints, intf)
    return interval

main()
