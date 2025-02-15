def makeMinute(time):
    [h, m] = time.split(":")
    return int(h) * 60 + int(m)

def parseMelody(melody):
    m = []
    for i in range(len(melody)):
        if melody[i] == '#':
            continue
        if i == len(melody) - 1 or melody[i+1] != '#':
            m.append(melody[i])
        else:
            m.append(melody[i] + melody[i+1])
    return m

def makeSong(melody, duration):
    parsedMelody = parseMelody(melody)
    mlen = len(parsedMelody)
    return [parsedMelody[i % mlen] for i in range(duration)]

def checkSublist(list1, list2):
    n = len(list2)
    return any(list1[i:i+n] == list2 for i in range(len(list1) - n + 1))

def solution(m, musicinfos):
    answer = ()
    for info in musicinfos:
        [start,end,title,melody] = info.split(",")
        duration = makeMinute(end) - makeMinute(start)
        song = makeSong(melody, duration)
        
        if not checkSublist(song, parseMelody(m)):
            continue
        if not answer:
            answer = (title, duration)
        elif answer[1] < duration:
            answer = (title, duration)
    
    if not answer:
        return "(None)"
    return answer[0]