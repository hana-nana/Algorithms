function solution(n) {
    let sum = 0;
    let strN = n.toString();
    for (let i = 0; i < strN.length; i++) {
        sum += Number(strN[i]);
    }
    return sum;
}