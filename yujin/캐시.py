from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cache = deque(maxlen=cacheSize)
    
    for city_str in cities:
        city = city_str.lower()
        
        if cacheSize != 0 and city in cache:
            cache.remove(city)
            cache.append(city)
            answer += 1
        else:
            cache.append(city)
            answer += 5
            
    return answer
