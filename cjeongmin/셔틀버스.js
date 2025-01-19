const START = 9 * 60;

const toMinutes = (time) => {
    const [hh, mm] = time.split(":").map(Number);
    return hh * 60 + mm;
};

const toHHMM = (minutes) => {
    const hh = String(Math.floor(minutes / 60)).padStart(2, "0");
    const mm = String(minutes % 60).padStart(2, "0");
    return `${hh}:${mm}`;
};

const canBoard = (n, t, m, x, crewTimes) => {
    let idx = 0;
    for (let i = 0; i < n; i++) {
        let capacity = m;
        const busTime = START + i * t;
        while (capacity > 0 && idx < crewTimes.length && crewTimes[idx] <= x && crewTimes[idx] <= busTime) {
            capacity--;
            idx++;
        }

        if (capacity > 0 && x <= busTime) return true;
    }
    return false;
};

function solution(n, t, m, timetable) {
    const crewTimes = timetable.map(toMinutes).sort((a, b) => a - b);

    let low = 0;
    let high = 23 * 60 + 59;
    let answer = START;
    while (low <= high) {
        const mid = Math.floor((low + high) / 2);
        if (canBoard(n, t, m, mid, crewTimes)) {
            answer = mid;
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }

    return toHHMM(answer);
}
