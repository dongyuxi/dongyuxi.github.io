---
layout: post
title: LeetCode 073 - Set Matrix Zeroes - 题解/Solution 
categories: 刷题
tags: leetcode java
keywords: leetcode,java,solution,题解,解题报告
tagline: Supporting tagline
---
***<https://leetcode.com/problems/set-matrix-zeroes/>***
<pre><code>/**
 * Given a m x n matrix, if an element is 0, set its entire row and column to 0.
 * Do it in place.
 * 
 * click to show follow up. Follow up:
 * 
 * Did you use extra space? A straight forward solution using O(mn) space is
 * probably a bad idea. A simple improvement uses O(m + n) space, but still not
 * the best solution. Could you devise a constant space solution?
 * 
 * 
 * @author dongyuxi
 *
 */
public class Solution {
    public void setZeroes(int[][] matrix) {
        if (null == matrix || 0 == matrix.length) {
            return;
        }

        int row = matrix.length;
        int col = matrix[0].length;
        boolean[] zeroRow = new boolean[row];
        boolean[] zeroCol = new boolean[col];
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (0 == matrix[i][j]) {
                    zeroRow[i] = true;
                    zeroCol[j] = true;
                }
            }
        }
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (zeroRow[i] || zeroCol[j]) {
                    matrix[i][j] = 0;
                }
            }
        }
    }
}
</code></pre>
