function solution(num) {
    if (num === 1) {
        return 0;
    }
    
    for (let count = 0; count < 501; count++) {
        if (num === 1) {
            return count;
            break
        } else if (count >= 500) {
            return -1
            break
        } else if (num % 2 === 0) {
            num = num / 2;
        } else if (num % 2 !== 0) {
            num = (num*3)+1;
        }
    }
}