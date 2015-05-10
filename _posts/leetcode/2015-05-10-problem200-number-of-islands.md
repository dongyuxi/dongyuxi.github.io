---
layout: post
title: LeetCode 200 - Number of Islands - 题解/Solution
categories: Leetcode
tags: leetcode java
keywords: leetcode,java,solution,题解,解题报告
tagline: Supporting tagline
---
***<https://leetcode.com/problems/number-of-islands/>***
<pre><code>/**
 * Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
 * An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
 * You may assume all four edges of the grid are all surrounded by water.
 * 
 * Example 1:

 * 11110
 * 11010
 * 11000
 * 00000
 * Answer: 1

 * Example 2:

 * 11000
 * 11000
 * 00100
 * 00011
 * Answer: 3
 * 
 * @author dongyuxi
 *
 */
public class Solution {
    public int numIslands(char[][] grid) {
        if (null == grid || 0 == grid.length || 0 == grid[0].length) {
            return 0;
        }
        int row = grid.length;
        int col = grid[0].length;
        int island = 0;
        boolean[][] visited = new boolean[row][col];
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (grid[i][j] == '1' && !visited[i][j]) {
                    island++;
                    Queue<Integer> rowQueue = new LinkedList<Integer>();
                    Queue<Integer> colQueue = new LinkedList<Integer>();
                    rowQueue.add(i);
                    colQueue.add(j);
                    while (!rowQueue.isEmpty()) {
                        int topRow = rowQueue.poll();
                        int topCol = colQueue.poll();
                        if (topRow - 1 >= 0 && grid[topRow - 1][topCol] == '1' && !visited[topRow - 1][topCol]) {
                            rowQueue.add(topRow - 1);
                            colQueue.add(topCol);
                            visited[topRow - 1][topCol] = true;
                        }
                        if (topRow + 1 < row && grid[topRow + 1][topCol] == '1' && !visited[topRow + 1][topCol]) {
                            rowQueue.add(topRow + 1);
                            colQueue.add(topCol);
                            visited[topRow + 1][topCol] = true;
                        }
                        if (topCol - 1 >= 0 && grid[topRow][topCol - 1] == '1' && !visited[topRow][topCol - 1]) {
                            rowQueue.add(topRow);
                            colQueue.add(topCol - 1);
                            visited[topRow][topCol - 1] = true;
                        }
                        if (topCol + 1 < col && grid[topRow][topCol + 1] == '1' && !visited[topRow][topCol + 1]) {
                            rowQueue.add(topRow);
                            colQueue.add(topCol + 1);
                            visited[topRow][topCol + 1] = true;
                        }
                    }
                }
            }
        }
        return island;
    }
}
</code></pre>
