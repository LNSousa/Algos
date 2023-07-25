/**
 * A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, 
 * it reads the same forward and backward. Alphanumeric characters include letters and numbers.
 * 
 * Given a string s, return true if it is a palindrome, or false otherwise.
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    let newS = s.toLowerCase().replace(/[^A-Za-z0-9]/g, "");

    for (let i = 0, j = newS.length-1; i <= j; i++, j--) {
        if (newS.charAt(i) != newS.charAt(j)) {
            return false;
        }
    }

    return true;
};

const s1 = "A man, a plan, a canal: Panama";
const s2 = "race a car";
const s3 = " ";
const s4 = "ab_a";

console.log(isPalindrome(s1))
console.log(isPalindrome(s2))
console.log(isPalindrome(s3))
console.log(isPalindrome(s4))