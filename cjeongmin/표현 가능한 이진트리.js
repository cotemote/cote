const padString = (binary) => {
    const originalLength = binary.length;
    let k = 0;
    while (Math.pow(2, k) - 1 < originalLength) {
        k += 1;
    }
    const totalLength = Math.pow(2, k) - 1;
    return binary.padStart(totalLength, '0');
};

const isValid = (s) => {
    if (s.length === 1) return true;
    
    const mid = Math.floor(s.length / 2);
    
    if (s[mid] === '0') {
        if (s.slice(0, mid).includes('1') || s.slice(mid + 1).includes('1')) {
            return false;
        }
    }
    
    return isValid(s.slice(0, mid)) && isValid(s.slice(mid + 1));
};

function solution(numbers) {
    return numbers.map((n) => (n).toString(2)).map(padString).map(isValid).map(Number);
}
