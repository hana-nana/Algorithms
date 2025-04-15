function solution(n) {
    let strN = n.toString();
    let answer = [];
    for (let i = strN.length-1; i >= 0 ; i--) {
        answer.push(Number(strN[i]));
    }
    return answer;
}