function solution(s1, s2) {
    var answer = 0;
//     console.log(s2.filter((a)=> s1.includes(a)).length)
//     return s2.filter((a)=> s1.includes(a)).length
    for (let i=0; i<s2.length; i++){
        for(let j=0; j<s1.length; j++){
            if(s2[i] === s1[j]){
               answer +=  1 }
    }
    }
    return answer
    
 }