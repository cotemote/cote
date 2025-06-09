N = int(input())

dp = [[[0] * 3 for _ in range(2)] for _ in range(N + 1)] 

dp[0][0][0] = 1 # 첫 날

for day in range(N):
    for late in range(2):
        for absent in range(3):
            count = dp[day][late][absent] # day일까지 late 만큼 지각하고 asbent 만큼 결석했을 때 출결 조합의 수
            dp[day + 1][late][0] = (dp[day + 1][late][0] + count) # 출석 / 결석 초기화
            if late == 0: # 지각
                dp[day + 1][late + 1][0] = (dp[day + 1][late + 1][0] + count)
            if absent < 2: # 결석
                dp[day + 1][late][absent + 1] = (dp[day + 1][late][absent + 1] + count)

result = 0

for late in range(2):
    for absent in range(3):
        result = (result + dp[N][late][absent])

print(result % 1000000)
