/**
 * Given an array of strings strs, group the anagrams together. 
 * You can return the answer in any order.
 * 
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
    let map = {};

    for (let str of strs) {
        let sortedWord = str.split('').sort().join('');

        if (map[sortedWord]) {
            map[sortedWord].push(str);
        } else {
            map[sortedWord] = [str]
        }
    }

    return Object.values(map)
};

console.log(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))