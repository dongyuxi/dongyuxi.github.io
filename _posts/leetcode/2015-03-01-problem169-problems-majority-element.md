---
layout: post
title: LeetCode 169 - Majority Element - 题解/Solution 
categories: Leetcode
tags: leetcode java
keywords: leetcode,java,solution,题解,解题报告
tagline: Supporting tagline
---
***<https://leetcode.com/problems/majority-element/>***
<pre><code>/**
 * Given an array of size n, find the majority element. The majority element is
 * the element that appears more than n / 2
 * 
 * You may assume that the array is non-empty and the majority element always
 * exist in the array.
 * 
 * @author dongyuxi
 *
 */
public class Solution {
    public int majorityElement(int[] num) {
        int count = 0;
        int majority = 0;
        for (int i = 0; i < num.length; i++) {
            if (0 == count) {
                majority = num[i];
                count++;
            } else {
                if (majority == num[i]) {
                    count++;
                } else {
                    count--;
                }
            }
        }
        return majority;
    }
}
</code></pre>