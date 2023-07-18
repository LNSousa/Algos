// Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

// After doing so, return the array.

/**
 * @param {number[]} arr
 * @return {number[]}
 */
var replaceElements = function(arr) {
    for (let i = 0; i < arr.length; i++) {
        if (i == arr.length-1) {
            arr[i] = -1
            return arr;
        }
        let max = 0;

        for (let j = i+1; j < arr.length; j++) {
            if(arr[j] > max) {
                max = arr[j];
            }
        }

        arr[i] = max;
    }
};

console.log(replaceElements([17,18,5,4,6,1]))
