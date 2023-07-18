/**
 * Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
 * 
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function(nums, k) {
    let map = {};
    for (let num of nums) {
        map[num] = (map[num] || 0) + 1;
    }

    let arr = Object.keys(map).sort(function(a, b) {
        return map[b] - map[a];
      });;

    return arr.splice(0, k)
};

console.log(topKFrequent(nums = [1,1,1,2,2,3], k = 2))
console.log(topKFrequent(nums = [4,1,-1,2,-1,2,3], k = 2))