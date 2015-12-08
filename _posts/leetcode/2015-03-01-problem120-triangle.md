---
layout: post
title: LeetCode 120 - Triangle - 题解/Solution 
categories: 刷题
tags: leetcode java
keywords: leetcode,java,solution,题解,解题报告
tagline: Supporting tagline
---
***<https://leetcode.com/problems/triangle/>***
<pre><code>/**
 * Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.
 * 
 * For example, given the following triangle
 * [
 *     [2],
 *    [3,4],
 *   [6,5,7],
 *  [4,1,8,3]
 * ]
 * The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
 * Note: Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
 * 
 * @author dongyuxi
 *
 */
public class Solution {
    public int minimumTotal(List<List<Integer>> triangle) {
        if (null == triangle || 0 == triangle.size()) {
            return 0;
        }
        int[] dp = new int[triangle.size()];
        for (int i = 0; i < triangle.size(); i++) {
            if (null == triangle.get(i)) {
                return 0;
            }
            for (int j = i; j >= 0; j--) {
                if (0 == i && 0 == j) {
                    dp[j] = triangle.get(i).get(j);
                } else {
                    if (j == 0) {
                        dp[j] = dp[j] + triangle.get(i).get(j);
                    } else if (j == i) {
                        dp[j] = dp[j - 1] + triangle.get(i).get(j);
                    } else {
                        dp[j] = Math.min(dp[j] + triangle.get(i).get(j),
                                            dp[j - 1] + triangle.get(i).get(j));
                    }
                }
            }
        }

        int min = Integer.MAX_VALUE;
        for (int i = 0; i < triangle.size(); i++) {
            if (dp[i] < min) {
                min = dp[i];
            }
        }

        return min;
    }
}
</code></pre>
