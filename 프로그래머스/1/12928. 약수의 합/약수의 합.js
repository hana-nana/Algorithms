function solution(n) {
    let answer = 0;
    let temp = 1;
    while (temp <= n) {
        if (n % temp === 0) {
            answer += temp;
        }
        temp++;
    }
    return answer;
}