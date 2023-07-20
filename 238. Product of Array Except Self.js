/**
 * Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i]. 
 * The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 * You must write an algorithm that runs in O(n) time and without using the division operation.
 * 
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
    let finalArr = new Array(nums.length).fill(1), prefix = 1, postfix = 1;

    for (let i = 0; i < nums.length; i++) {
        finalArr[i] = prefix;
        prefix *= nums[i];
    }

    for (let i = nums.length -1; i >= 0; i--) {
        finalArr[i] *= postfix;
        postfix *= nums[i]
    }

    return finalArr
};

console.log(productExceptSelf([1,2,3,4]))
console.log(productExceptSelf([-1,1,0,-3,3]))