/**
 * @param {number} x
 * @return {number}
 */
var reverse = function(x) {
    var numArrayReversed = x.toString().split('').reverse()
    var solution 
    if (numArrayReversed[numArrayReversed.length-1] === '-'){
        solution = -Math.abs(parseInt(numArrayReversed.join('')));
    } else{
        solution = parseInt(numArrayReversed.join(''));
    }
    if ((-2)**31 <= solution && solution <= 2**31 -1){
        return solution
    }else{
        return 0
    }
};