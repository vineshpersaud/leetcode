/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    for (var i = 0; i< nums.length; i++){
        otherNum = nums.indexOf(target - nums[i])
        if (otherNum !== -1 && otherNum !== i){
           return [i,nums.indexOf(target - nums[i])]
        }
    }
       
};