/**
 * Given a string s consisting of words and spaces, return the length of the last word in the string.
 * 
 * A word is a maximal substring consisting of non-space characters only.
 * 
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) {
    let sLngt = s.length-1, wordLength = 0;

    while (s.charAt(sLngt) == " ") {
        sLngt--;
    }

    while (s.charAt(sLngt) != " " && sLngt >= 0) {
        wordLength++;
        sLngt--;
    }

    return wordLength;
};





console.log(lengthOfLastWord("Hello World"));
console.log(lengthOfLastWord("   fly me   to   the moon  "));
console.log(lengthOfLastWord("luffy is still joyboy"));
console.log(lengthOfLastWord("a"));