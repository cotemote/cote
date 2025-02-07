const splitSheet = (sheet) => {
    const result = [];
    for (let i = 0; i < sheet.length; i++) {
        if (sheet[i + 1] === "#") {
            result.push(sheet.slice(i, i + 2));
            i++;
        } else {
            result.push(sheet[i]);
        }
    }
    return result;
};

const toMinutes = (time) => Number(time.slice(0, 2)) * 60 + Number(time.slice(3));

const parse = (musicinfo) => {
    const [start, end, title, sheet] = musicinfo.split(",");
    const duration = toMinutes(end) - toMinutes(start);
    const tokens = splitSheet(sheet);
    const fullSheet = Array.from({ length: duration }, (_, i) => tokens[i % tokens.length]);
    return { title, duration, sheet: fullSheet };
};

const match = (m1, info) => {
    const pattern = "," + m1.join(",") + ",";
    const sheetStr = "," + info.sheet.join(",") + ",";
    return sheetStr.indexOf(pattern) !== -1;
};

function solution(m, musicinfos) {
    const m1 = splitSheet(m);

    const result = musicinfos.map(parse).filter((m2) => match(m1, m2));

    if (result.length === 0) return "(None)";

    return result.sort((a, b) => b.duration - a.duration)[0].title;
}
