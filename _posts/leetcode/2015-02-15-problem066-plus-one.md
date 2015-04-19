---
layout: post
title: LeetCode 066 - Plus One - 题解/Solution 
categories: Leetcode
tags: leetcode java
keywords: leetcode,java,solution,题解,解题报告
tagline: Supporting tagline
---
***<https://leetcode.com/problems/plus-one/>***
<pre><code>/**
 * Given a non-negative number represented as an array of digits, plus one to
 * the number.
 * 
 * The digits are stored such that the most significant digit is at the head of
 * the list.
 * 
 * @author dongyuxi
 *
 */
public class Solution {
    public int[] plusOne(int[] digits) {
        if (null == digits || 0 == digits.length) {
            return digits;
        }

        int[] temp = new int[digits.length];
        int index = 0;
        int pass = 0, add = 1;
        for (int i = digits.length - 1; i >= 0; i--) {
            temp[index++] = (digits[i] + add + pass) % 10;
            pass = (digits[i] + add + pass) / 10;
            add = 0;
        }

        int[] result = null;
        if (1 == pass) {
            result = new int[digits.length + 1];
            result[0] = 1;
        } else {
            result = new int[digits.length];
        }
        index = result.length - 1;
        for (int i = 0; i < temp.length; i++) {
            result[index--] = temp[i];
        }
        return result;
    }
}
</code></pre>