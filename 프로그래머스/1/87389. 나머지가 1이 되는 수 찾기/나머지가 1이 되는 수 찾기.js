function solution(n) {
    let x = 0;
    let arr = [];
    while (x >= 0) {
     if (n % x === 1) {
        arr.push(x);
        break
     }
     x += 1;
    }
    return arr[0];
}