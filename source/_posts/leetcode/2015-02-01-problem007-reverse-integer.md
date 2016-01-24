---
layout: post
title: LeetCode 007 - Reverse Integer  - 题解/Solution
categories: 刷题
tags: [leetcode,java]
keywords: leetcode,java,solution,题解,解题报告
date: 2015-02-01
permalink: problem007-reverse-integer
---
***<https://leetcode.com/problems/reverse-integer/>***
<!--more-->
```java
/**
 * Reverse digits of an integer.
 * 
 * Example1: x = 123, return 321 Example2: x = -123, return -321
 * 
 * click to show spoilers.
 * 
 * Have you thought about this? Here are some good questions to ask before
 * coding. Bonus points for you if you have already thought through this!
 * 
 * If the integer's last digit is 0, what should the output be? ie, cases such
 * as 10, 100.
 * 
 * Did you notice that the reversed integer might overflow? Assume the input is
 * a 32-bit integer, then the reverse of 1000000003 overflows. How should you
 * handle such cases?
 * 
 * For the purpose of this problem, assume that your function returns 0 when the
 * reversed integer overflows.
 * 
 * @author dongyuxi
 *
 */
public class Solution {
    public int reverse(int x) {
        long l = (long)x;
        boolean minus = false;
        if (l < 0) {
            minus = true;
            l = -l;
        }
        String s = Long.toString(l);
        StringBuilder sb = new StringBuilder();
        boolean zero = true;
        for (int i = s.length() - 1; i >= 0; i--) {
            if ('0' != s.charAt(i)) {
                zero = false;
            }
            if (zero) {
                continue;
            }
            sb.append(s.charAt(i));
        }
        if (sb.length() == 0) {
            return 0;
        }
        l = Long.parseLong(sb.toString());
        if (minus) {
            l = -l;
        }
        if (l > Integer.MAX_VALUE || l < Integer.MIN_VALUE) {
            return 0;
        }
        return (int)l;
    }
}
```