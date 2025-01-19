def solution(n, t, m, timetable):
    answer = ''
    bus_time = []
    passengers = []
    passengers_info = []
    init = 9*60
    for i in range(n) :
        bus_time.append(init + t * i)
    
    for time in timetable :
        [H, M] = map(int, time.split(':'))
        tm = H * 60 + M
        passengers_info.append(tm)
    passengers_info.sort()
    
    for i in range(len(bus_time)) :
        passengers = []
        while passengers_info and passengers_info[0] <= bus_time[i] and len(passengers) < m :
            passengers.append(passengers_info.pop(0))
    
    if len(passengers) < m:
        answer_time = bus_time[-1]
    else:
        answer_time = passengers[-1] - 1

    answer = f'{answer_time // 60:02}:{answer_time % 60:02}'
    return answer