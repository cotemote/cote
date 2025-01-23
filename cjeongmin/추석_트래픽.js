const parseTimeToMilliseconds = (timeStr) => {
    const [hh, mm, ss] = timeStr.split(":");
    return +hh * 3600000 + +mm * 60000 + parseFloat(ss) * 1000;
};

const parseLog = (line) => {
    const [_, endTimeStr, durationStr] = line.split(" ");
    const endTime = parseTimeToMilliseconds(endTimeStr);
    const duration = parseFloat(durationStr.slice(0, -1)) * 1000;
    const startTime = endTime - duration + 1;

    return [startTime, endTime];
};

const countOverlappingLogs = (timestamp, logs) => {
    const windowEnd = timestamp + 999;
    return logs.filter(([start, end]) => end >= timestamp && start <= windowEnd).length;
};

function solution(lines) {
    const processedLogs = lines.map(parseLog);
    const endTimestamps = processedLogs.map(([_, end]) => end);

    return Math.max(...endTimestamps.map((time) => countOverlappingLogs(time, processedLogs)));
}
