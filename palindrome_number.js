var isPalindrome = function(x) {
    stringed_array = String(x).split('');
    return stringed_array.join('') === stringed_array.reverse().join('');
    
};