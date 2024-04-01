function solution(my_string) {
    var answer = 0;
    for (let i = 0; i < my_string.length; i++) {
        const num = Number(my_string[i]);
        if (!isNaN(num)) { 
            answer += num;
        } else {
            answer += 0; 
        }
    }
    return answer;
}
