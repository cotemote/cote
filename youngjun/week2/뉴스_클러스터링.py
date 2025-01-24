from collections import Counter

def strConverter(s):
    arr = []
    for i in range(len(s)-1):
        elem = ''
        if s[i].isalpha() == False or s[i+1].isalpha() == False:
            continue
        elem += s[i].upper()
        elem += s[i+1].upper()
        arr.append(elem)
    return arr
    
def multi_intersection(arr1, arr2):
    counter1 = Counter(arr1)
    counter2 = Counter(arr2)
    common_counter = counter1 & counter2  # 요소의 빈도 중 최소값만 유지
    return list(common_counter.elements())

def multi_union(arr1, arr2):
    counter1 = Counter(arr1)
    counter2 = Counter(arr2)
    union_counter = counter1 | counter2  # 요소의 빈도 중 최대값만 유지
    return list(union_counter.elements())    

def jaccard(arr1, arr2):
    kyo = multi_intersection(arr1,arr2)
    hap = multi_union(arr1, arr2)
    print('kyo: ', kyo, 'hap: ',hap)
    if len(hap) == 0:
        return 1
    return len(kyo)/len(hap)


def solution(str1, str2):
    arr1 = strConverter(str1)
    arr2 = strConverter(str2)
    
    answer = int(jaccard(arr1,arr2) * 65536)
    
    
    return answer
