function solution(arr) {
   let answer = arr.reduce((sum, digit) => sum + digit) / arr.length;
    return answer;
}