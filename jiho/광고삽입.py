def make_sec(time):
    nums = list(map(int, time.split(":")))
    return nums[0] * 3600 + nums[1] * 60 + nums[2]


def make_time(sec):
    h = sec // 3600
    m = sec // 60 % 60
    s = sec % 60
    return ":".join([str(h).zfill(2), str(m).zfill(2), str(s).zfill(2)])


def solution(play_time, adv_time, logs):
    play_time = make_sec(play_time)
    adv_time = make_sec(adv_time)
    all_time = [0] * (play_time + 1)

    for log in logs:
        start, end = log.split("-")
        start = make_sec(start)
        end = make_sec(end)
        all_time[start] += 1
        all_time[end] -= 1

    for i in range(1, len(all_time)):
        all_time[i] = all_time[i] + all_time[i - 1]

    for i in range(1, len(all_time)):
        all_time[i] = all_time[i] + all_time[i - 1]

    most_view = 0
    max_time = 0
    for i in range(adv_time - 1, play_time):
        if i >= adv_time:
            if most_view < all_time[i] - all_time[i - adv_time]:
                most_view = all_time[i] - all_time[i - adv_time]
                max_time = i - adv_time + 1
        else:
            if most_view < all_time[i]:
                most_view = all_time[i]
                max_time = i - adv_time + 1

    return make_time(max_time)
