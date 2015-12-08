---
layout: post
title: LeetCode 130 - Surrounded Regions - 题解/Solution
categories: 刷题
tags: leetcode java
keywords: leetcode,java,solution,题解,解题报告
tagline: Supporting tagline
---
***<https://leetcode.com/problems/surrounded-regions/>***
<pre><code>/**
 * Given a 2D board containing 'X' and 'O', capture all regions surrounded by 'X'.
 *
 * A region is captured by flipping all 'O's into 'X's in that surrounded region.
 * 
 * For example,
 * X X X X
 * X O O X
 * X X O X
 * X O X X
 * After running your function, the board should be:
 * 
 * X X X X
 * X X X X
 * X X X X
 * X O X X
 * 
 * @author dongyuxi
 * 
 */
public class Solution {
    public void solve(char[][] board) {
        if (null == board || 0 == board.length || 0 == board[0].length) {
            return;
        }
        int row = board.length;
        int col = board[0].length;
        boolean[][] unsurrounded = new boolean[row][col];
        for (int i = 0; i < col; i++) {
            if (!unsurrounded[0][i] && board[0][i] == 'O') {
                bfs(board, unsurrounded, 0, i);
            }
        }
        for (int i = 0; i < col; i++) {
            if (!unsurrounded[row - 1][i] && board[row - 1][i] == 'O') {
                bfs(board, unsurrounded, row - 1, i);
            }
        }
        for (int i = 0; i < row; i++) {
            if (!unsurrounded[i][0] && board[i][0] == 'O') {
                bfs(board, unsurrounded, i, 0);
            }
        }
        for (int i = 0; i < row; i++) {
            if (!unsurrounded[i][col - 1] && board[i][col - 1] == 'O') {
                bfs(board, unsurrounded, i, col - 1);
            }
        }
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (board[i][j] == 'O' && !unsurrounded[i][j]) {
                    board[i][j] = 'X';
                }
            }
        }
    }

    private void bfs(char[][] board, boolean[][] unsurrounded, int row, int col) {
        if (unsurrounded[row][col]) {
            return;
        }
        Queue<Integer> rowQueue = new LinkedList<Integer>();
        Queue<Integer> colQueue = new LinkedList<Integer>();
        rowQueue.add(row);
        colQueue.add(col);
        while (!rowQueue.isEmpty()) {
            int r = rowQueue.poll();
            int c = colQueue.poll();
            unsurrounded[r][c] = true;
            if (r - 1 >= 0 && board[r - 1][c] == 'O' && !unsurrounded[r - 1][c]) {
                rowQueue.add(r - 1);
                colQueue.add(c);
                unsurrounded[r - 1][c] = true;
            }
            if (r + 1 < board.length && board[r + 1][c] == 'O' && !unsurrounded[r + 1][c]) {
                rowQueue.add(r + 1);
                colQueue.add(c);
                unsurrounded[r + 1][c] = true;
            }
            if (c - 1 >= 0 && board[r][c - 1] == 'O' && !unsurrounded[r][c - 1]) {
                rowQueue.add(r);
                colQueue.add(c - 1);
                unsurrounded[r][c - 1] = true;
            }
            if (c + 1 < board[0].length && board[r][c + 1] == 'O' && !unsurrounded[r][c + 1]) {
                rowQueue.add(r);
                colQueue.add(c + 1);
                unsurrounded[r][c + 1] = true;
            }
        }
    }
}
</code></pre>
