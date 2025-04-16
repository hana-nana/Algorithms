function solution(N, stages) {
    let result = [];
    
    for (let stage = 1; stage <= N; stage++) {
        // 해당 스테이지에 멈춰있는 사람
        let stuck = 0;
        // 해당 스테이지에 도달한 사람
        let reached = 0;
        
        for (let i = 0; i < stages.length; i++) {
            if (stages[i] >= stage) {
                reached++;
            }
            if (stages[i] === stage) {
                stuck++;
            }
        }
    
    // 도달한 사람 1명이라도 있으면 실패율 계산
    // 도달한 사람 없으면 실패율은 0으로 간주
    let failRate = 0;
    if (reached !== 0) {
        failRate = stuck / reached;
    }
    result.push([stage, failRate]);
    
    }
    
    // 실패율 기준 내림차순 정렬, 같으면 스테이지 번호 오름차순
    for (let i = 0; i < result.length-1; i++) {
        for (let j = i+1; j < result.length; j++) {
            let cur = result[i];
            let next = result[j];
            
            if (
                // 실패율이 뒤에거가 크거나 -> swap대상
                (next[1] > cur[1]) ||
                // 실패율이 뒤에거랑 같다면, 뒤에거 스테이번호가 낮을경우 -> swap 대상
                (next[1] === cur[1] && next[0] < cur[0])
            ) {
                // swap 하기
                let temp = result[i];
                result[i] = result[j];
                result[j] = temp;
            }
        }
    }
    
    // 행만 바꿔가면서 첫번째 열[0]만 추출 -> 스테이지 번호만 나오도록
    let answer = [];
    for (let i = 0; i < result.length; i++) {
        answer.push(result[i][0]);
    }
    
    return answer;
    
}