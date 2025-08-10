function solution(n, bans) {
    
    const strToIndex = (str) => {
        let num = 0;
        for (let i = 0; i < str.length; i++) {
            num = num * 26 + (str.charCodeAt(i) - 96);
        }
        return num;
    };
    
    const bannedNums = bans.map(strToIndex);
    bannedNums.sort((a, b) => a - b);
    
    const indexToStr = (index) => {
      let s = "";
      while (index > 0) {
        index--;
        const r = index % 26;
        s = String.fromCharCode(97 + r) + s;
        index = Math.floor(index / 26);
      }
      return s;
    };
    
    let target = n;
    for (let i = 0; i < bannedNums.length; i++) {
        if (bannedNums[i] <= target) target++;
        else break;
    }

    return indexToStr(target);
}
