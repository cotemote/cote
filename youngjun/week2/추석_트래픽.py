# answer의 max 값은 len(lines)
# answer는 무조건 특정 로그의 시작 혹은 끝 시점
# 답이 될 수 있는 구간을 intervals 딕셔너리로 만들고, 각 로그에 대해 범위가 겹치는 구간의 카운트를 1씩 올리면 구할 수 있음


def logSplit(lines):
    endTime = []
    duration = []
    for line in lines:
        logs = line.split()
        endTime.append(logs[1])
        duration.append(float(logs[2][:-1]))
    return endTime, duration

def timeToFloat(time):
    h = int(time[0:2])
    m = int(time[3:5]) 
    s = float(time[6:])
    return h*3600 + m*60 + s

def intervalMaker(endTime, duration):
    intervals = {}
    times = []  # (start, end) 저장
    for i in range(len(endTime)):
        end = round(timeToFloat(endTime[i]), 3)
        start = round(end - duration[i] + 0.001, 3)
        times.append((start, end))
        intervals[start] = 0
        intervals[end] = 0
    return intervals, times

def solution(lines):
    endTime, duration = logSplit(lines)
    intervals, times = intervalMaker(endTime, duration)
    for start, end in times:
        for key in intervals.keys():
            if key <= end and key + 1 > start:
                intervals[key] += 1
    return max(intervals.values())