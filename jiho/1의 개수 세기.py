A, B = map(int, input().split())

digit = [0] * (54 + 1)  # 10^16은 2진수로 54자리
for i in range(1, len(digit)):
    cnt = pow(2, i - 1)
    digit[i] = cnt + (i - 1) * (cnt // 2) + digit[i - 1]


def count_1(num):
    global digit

    if num == 0:
        return 0

    bin_num = bin(num)[2:]
    prev_digit_cnt = digit[len(bin_num) - 1]

    bin_num = bin_num[1:]
    while len(bin_num) > 0:
        if bin_num[0] == "1":
            break
        bin_num = bin_num[1:]

    if len(bin_num) == 0:
        now_digit_cnt = 1
    else:
        sub_num = int("0b" + bin_num, 2)
        now_digit_cnt = count_1(sub_num) + sub_num + 1

    return prev_digit_cnt + now_digit_cnt


print(count_1(B) - count_1(A - 1))
