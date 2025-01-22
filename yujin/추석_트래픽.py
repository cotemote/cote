 # 각 항목의 1초 간격 동안 얼마나 많이 있는지 카운트
def solution(lines):
    answer = 0
    
    if len(lines) == 1:
        return 1
    
    for index, line in enumerate(lines):
        date, time, T = line.split()

        max_end = get_day_ms(date) + get_time_ms(time)
        
        count = 1
        
        for x in range(index + 1, len(lines)):
            date2, time2, T2 = lines[x].split()
            other_end = get_day_ms(date2) + get_time_ms(time2)
            
            other_start = other_end - float(T2[:-1]) + 0.001
            if max_end + 1 <= other_end - 3:
                break
            if max_end + 1 > other_start:
                count += 1
    
        if answer < count:
            answer = count
        
    return answer

def get_time_ms(time):
    H, M, S = map(float, time.split(":"))
    return S + M * 60 + H * 3600

def get_day_ms(date):
    year, month, day = map(int, date.split("-"))
    return day * 2 * 3600
    
    
