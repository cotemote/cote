def solution(n, t, m, timetable):
    avaliable = []
    times = []
    start_time = 9 * 60
    
    for time in timetable:
        [hours, minutes] = time.split(":")
        times.append(60 * int(hours) + int(minutes))
    
    times.sort(reverse=True)
        
    for count in range(n):
        avaliable.append([])
        while len(times) > 0 and len(avaliable[count]) < m and start_time + count * t >= times[-1]:
            avaliable[count].append(times.pop())
    
    print(avaliable)
    
    if len(avaliable[-1]) < m:
        return formatted(start_time + (n - 1) * t) 
    else:
        return formatted(avaliable[-1][-1] - 1)
    

def formatted(time):
    return f"{time // 60:02}:{time % 60:02}"
