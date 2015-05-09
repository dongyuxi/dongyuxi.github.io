---
layout: post
title: LeetCode 137 - Single Number II - 题解/Solution
categories: Leetcode
tags: leetcode java
keywords: leetcode,java,solution,题解,解题报告
tagline: Supporting tagline
---
***<https://leetcode.com/problems/single-number-ii/>***
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
        if (null == A || 1 != A.length % 3) {
            return 0;
        }

        int result = 0;
        for (int i = 0; i < 32; i++) {
            int bitCount = 0;
            for (int j = 0; j < A.length; j++) {
                if (((A[j] >> i) & 0x01) == 1) {
                    bitCount++;
                }
            }
            result |= (bitCount % 3) << i;
        }

        return result;
    }
}
</code></pre>
