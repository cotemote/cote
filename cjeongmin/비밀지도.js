function solution(n, arr1, arr2) {
    return Array.from({ length: n })
        .map((_, i) => (arr1[i] | arr2[i]).toString(2).padStart(n, "0"))
        .map((v) => v.replaceAll("1", "#").replaceAll("0", " "));
}
