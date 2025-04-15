function solution(n)
{
    return n
        .toString()
        .split('')
        .reduce((sum, num) => {
            return sum + Number(num);    
        }, 0);
}