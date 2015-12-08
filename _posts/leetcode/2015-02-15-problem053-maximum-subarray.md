---
layout: post
title: LeetCode 053 - Maximum Subarray - 题解/Solution 
categories: 刷题
tags: leetcode java
keywords: leetcode,java,solution,题解,解题报告
tagline: Supporting tagline
---
***<https://leetcode.com/problems/maximum-subarray/>***
<pre><code>/**
 * Find the contiguous subarray within an array (containing at least one number)
 * which has the largest sum.
 * 
 * For example, given the array [-2,1,-3,4,-1,2,1,-5,4], the contiguous subarray
 * [4,-1,2,1] has the largest sum = 6.
 * 
 * click to show more practice.
 * 
 * More practice: If you have figured out the O(n) solution, try coding another
 * solution using the divide and conquer approach, which is more subtle.
 * 
 * @author dongyuxi
 * 
 */
public class Solution {
    public int maxSubArray(int[] A) {
        if (null == A || 0 == A.length) {
            return 0;
        }

        int cur = A[0];
        int max = A[0];
        for (int i = 1; i < A.length; i++) {
            if (cur < 0) {
                cur = A[i];
            } else {
                cur += A[i];
            }
            if (cur > max) {
                max = cur;
            }
        }

        return max;
    }
}
</code></pre>
