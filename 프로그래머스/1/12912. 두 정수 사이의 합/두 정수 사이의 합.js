function solution(a, b) {
    let start = a;
    let end = b;
    if (a > b) {
        start = b;
        end = a;
    }
    
    let sum = 0;
    for (let i = start; i <= end; i++) {
        sum += i;
    }
    return sum;
}