def solution(n, arr1, arr2):
    map1 = [[0 for j in range(n)] for i in range(n)]
    map2 = [[0 for j in range(n)] for i in range(n)]
    row = 0
    
    for i in range(n):
        row = format(arr1[i],'b')
        for j in range(len(row)):
            map1[i][n-1-j] = row[len(row)-j-1]
    
    for i in range(n):
        row = format(arr2[i],'b')
        for j in range(len(row)):
            map2[i][n-1-j] = row[len(row)-j-1]
    
    answer = []

    result = ''

    for k in range(n):
        for t in range(n):

            if int(map1[k][t]) == 1 or int(map2[k][t]) == 1:
                result+='#'
            else:
                result+=' '
        answer.append(result)
        result = ''
    
    
    return answer