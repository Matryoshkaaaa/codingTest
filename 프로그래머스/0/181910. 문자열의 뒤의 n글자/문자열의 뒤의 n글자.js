function solution(my_string, n) {
    var answer = [...my_string];
    let result = [];
    for(let i=answer.length-n; i<answer.length; i++)
        {
            result.push(answer[i])
            
        }
    console.log(result);
    return result.join('');
}