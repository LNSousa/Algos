/**
 * Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
 * 
 * 1. Each row must contain the digits 1-9 without repetition.
 * 
 * 2. Each column must contain the digits 1-9 without repetition.
 * 
 * 3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
 * 
 * Note:
 * A Sudoku board (partially filled) could be valid but is not necessarily solvable.
 * 
 * Only the filled cells need to be validated according to the mentioned rules.
 * 
 * @param {character[][]} board
 * @return {boolean}
 */
var isValidSudoku = function(board) {
    const rows=[],cols=[],box = [];

    for (let i = 0; i < 9; i ++) {
        rows.push(new Set())
        cols.push(new Set())
        box.push(new Set())
    }

    
    for (let r = 0; r < 9; r++) {
        for (let c = 0; c < 9; c++) {
            const value = board[r][c];
            if (value === ".") continue;
            const boxIndx = Math.floor(r / 3) * 3 + Math.floor(c / 3);
            if(rows[r].has(value) || cols[c].has(value) || box[boxIndx].has(value)) return false;
            rows[r].add(value);
            cols[c].add(value);
            box[boxIndx].add(value);
        }
    }
    return true;
};




let board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

let falseBoard = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

console.log(isValidSudoku(board));
console.log(isValidSudoku(falseBoard));