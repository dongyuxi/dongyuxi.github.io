---
layout: post
title: LeetCode 136 - Single Number - 题解/Solution 
categories: 刷题
tags: leetcode java
keywords: leetcode,java,solution,题解,解题报告
tagline: Supporting tagline
---
***<https://leetcode.com/problems/single-number/>***
<pre><code>/**
 * Given an array of integers, every element appears three times except for one.
 * Find that single one.
 * 
 * Note: Your algorithm should have a linear runtime complexity. Could you
 * implement it without using extra memory?
 * 
 * @author dongyuxi
 * 
 */
public class Solution {
    public int singleNumber(int[] A) {
        if (null == A || 0 == A.length % 2) {
            return 0;
        }

        int result = A[0];
        for (int i = 1; i < A.length; i++) {
            result ^= A[i];
        }

        return result;
    }
}
</code></pre>
