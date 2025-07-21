import sys
input = sys.stdin.readline

def count_ones_upto(N):
    total = 0 # 1의 개수
    i = 0 # 2^i가 N보다 작거나 같을 때까지 반복
    while (1 << i) <= N:
        cycle = 1 << (i + 1)           # 2^(i+1)
        full = (N + 1) // cycle        # 꽉 찬 주기 개수(0부터 세는 거라서 + 1함)
        ones_in_full = full * (1 << i) # 꽉 찬 주기에서의 1 개수
        
        rem = (N + 1) % cycle # 싸이클을 돈 것을 제외한 수
        ones_in_rem = max(0, rem - (1 << i))
        
        total += ones_in_full + ones_in_rem # 주기 x 주기 안에서 1의 개수 + 남은 1의 개수
        i += 1
    return total

def solve():
    A, B = map(int, input().split())
    # B까지 구한 1의 개수에서 A - 1까지 구한 1의 개수를 빼면 A부터 B까지 숫자의 1의 개수를 구할 수 있음
    answer = count_ones_upto(B) - count_ones_upto(A-1)
    print(answer)

if __name__ == "__main__":
    solve()
