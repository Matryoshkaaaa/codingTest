function solution(array) {
    var answer = 0;
    
    array.sort((a,b)=>a-b);
    console.log(array[Math.floor(array.length/2)])
    return(array[Math.floor(array.length/2)])
    
}