function solution(phone_number) {
    let answer = '';
    const len = phone_number.length;
    
    for (let i = 0; i < len; i++) {
        if (i < len - 4) {
            answer += '*'
        } else {
            answer += phone_number[i];
        }
    }
    return answer;
}

// <추가 풀이방법>
// function solution(phone_number) {
//     const masked = "*".repeat(phone_number.length - 4);
//     const last4 = phone_number.slice(-4);
//     return masked + last4;
// }
