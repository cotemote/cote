function solution(record) {
    const sentence = { Enter: "님이 들어왔습니다.", Leave: "님이 나갔습니다." };
    const { nicknames, log } = record.reduce(
        (acc, rec) => {
            const [cmd, uid, nickname] = rec.split(" ");
            if (nickname) acc.nicknames[uid] = nickname;
            if (cmd !== "Change") acc.log.push({ cmd, uid });
            return acc;
        },
        { nicknames: {}, log: [] }
    );
    return log.map(({ cmd, uid }) => `${nicknames[uid]}${sentence[cmd]}`);
}
