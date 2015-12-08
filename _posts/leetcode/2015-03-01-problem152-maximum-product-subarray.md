---
layout: post
title: LeetCode 152 - Maximum Product Subarray - 题解/Solution 
categories: 刷题
tags: leetcode java
keywords: leetcode,java,solution,题解,解题报告
tagline: Supporting tagline
---
***<https://leetcode.com/problems/maximum-product-subarray/>***
<pre><code>/**
 * Find the contiguous subarray within an array (containing at least one number)
 * which has the largest product.
 * 
 * For example, given the array [2,3,-2,4], the contiguous subarray [2,3] has
 * the largest product = 6.
 * 
 * @author dongyuxi
 *
 */
public class Solution {
    public int maxProduct(int[] A) {
        if (null == A || 0 == A.length) {
            return 0;
        }

        int max = A[0], curMax = A[0], curMin = A[0];
        for (int i = 1; i < A.length; i++) {
            int tempMax = curMax * A[i];
            int tempMin = curMin * A[i];
            curMax = Math.max(A[i], Math.max(tempMin, tempMax));
            curMin = Math.min(A[i], Math.min(tempMin, tempMax));
            max = Math.max(max, curMax);
        }
        return max;
    }
}
</code></pre>
