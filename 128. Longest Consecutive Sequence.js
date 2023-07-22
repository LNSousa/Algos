/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function(nums) {
    let set = new Set(nums), longest = 0;

    for (let num of set) {
        if (!set.has(num - 1)) {
            let length = 0;
            while (set.has(num + length)) {
                length++;
            }
            longest = Math.max(longest, length);
        }
    }
    return longest;
};



let nums1 = [100,4,200,1,3,2]
let nums2 = [0,3,7,2,5,8,4,6,0,1]

console.log(longestConsecutive(nums1))
console.log(longestConsecutive(nums2))