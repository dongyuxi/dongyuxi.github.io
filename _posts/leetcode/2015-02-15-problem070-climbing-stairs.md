---
layout: post
title: LeetCode 070 - Climbing Stairs - 题解/Solution 
categories: 刷题
tags: leetcode java
keywords: leetcode,java,solution,题解,解题报告
tagline: Supporting tagline
---
***<https://leetcode.com/problems/climbing-stairs/>***
<pre><code>/**
 * You are climbing a stair case. It takes n steps to reach to the top.
 * 
 * Each time you can either climb 1 or 2 steps. In how many distinct ways can
 * you climb to the top?
 * 
 * @author dongyuxi
 *
 */
public class Solution {
    public int climbStairs(int n) {
        if (0 == n || 1 == n) {
            return 1;
        }
        int num1 = 1;
        int num2 = 1;
        for (int i = 2; i <= n; i++) {
            int temp = num2;
            num2 = num1 + num2;
            num1 = temp;
        }
        return num2;
    }
}
</code></pre>
