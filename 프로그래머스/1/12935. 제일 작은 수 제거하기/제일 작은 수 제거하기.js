function solution(arr) {
    const minNum = Math.min(...arr);
    const filtered = arr.filter((elem) => elem !== minNum)
    if (1 >= arr.length) {
        return [-1];
    } else {
        return filtered;
    }
}