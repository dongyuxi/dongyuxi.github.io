---
layout: post
title: LeetCode 191 - Number of 1 Bits - 题解/Solution
categories: Leetcode
tags: leetcode java
keywords: leetcode,java,solution,题解,解题报告
tagline: Supporting tagline
---
***<https://leetcode.com/problems/number-of-1-bits/>***
<pre><code>/**
 * Write a function that takes an unsigned integer and returns the number of ’1'
 * bits it has (also known as the Hamming weight).
 * 
 * For example, the 32-bit integer ’11' has binary representation
 * 00000000000000000000000000001011, so the function should return 3.
 * 
 * @author dongyuxi
 *
 */
public class Solution {
    // you need to treat n as an unsigned value
    public int hammingWeight(int n) {
        int weight = 0;
        while (0 != n) {
            n = n & (n - 1);
            weight++;
        }
        return weight;
    }
}
</code></pre>
