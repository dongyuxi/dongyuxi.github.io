---
layout: post
title: LeetCode 064 - Minimum Path Sum - 题解/Solution 
categories: 刷题
tags: leetcode java
keywords: leetcode,java,solution,题解,解题报告
tagline: Supporting tagline
---
***<https://leetcode.com/problems/minimum-path-sum/>***
<pre><code>/**
 * Given a m x n grid filled with non-negative numbers, find a path from top
 * left to bottom right which minimizes the sum of all numbers along its path.
 * 
 * Note: You can only move either down or right at any point in time.
 * 
 * @author dongyuxi
 *
 */
public class Solution {
    public int minPathSum(int[][] grid) {
        if (null == grid || 0 == grid.length) {
            return 0;
        }

        int m = grid.length;
        int n = grid[0].length;
        int[][] dp = new int[m][n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (0 == i && j == 0) {
                    dp[i][j] = grid[i][j];
                } else if (0 == i) {
                    dp[i][j] = dp[i][j - 1] + grid[i][j];
                } else if (0 == j) {
                    dp[i][j] = dp[i - 1][j] + grid[i][j];
                } else {
                    dp[i][j] = Math.min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j];
                }
            }
        }

        return dp[m - 1][n - 1];
    }
}
</code></pre>
