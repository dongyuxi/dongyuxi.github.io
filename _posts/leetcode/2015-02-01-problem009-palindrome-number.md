---
layout: post
title: LeetCode 009 - Palindrome Number  - 题解/Solution
categories: Leetcode
tags: leetcode java
keywords: leetcode,java,solution,题解,解题报告
tagline: Supporting tagline
---
***<https://leetcode.com/problems/palindrome-number/>***
<pre><code>/**
 * Determine whether an integer is a palindrome. Do this without extra space.
 * 
 * Could negative integers be palindromes? (ie, -1)
 * 
 * If you are thinking of converting the integer to string, note the restriction
 * of using extra space.
 * 
 * You could also try reversing an integer. However, if you have solved the
 * problem "Reverse Integer", you know that the reversed integer might overflow.
 * How would you handle such case?
 * 
 * There is a more generic way of solving this problem.
 * 
 * @author dongyuxi
 *
 */
public class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0) {
            return false;
        }

        if (x == 0) {
            return true;
        }

        int base = 1;
        while (x / base >= 10) {
            base *= 10;
        }

        while (x > 0) {
            int left = x / base;
            int right = x % 10;
            if (left != right) {
                return false;
            }
            x -= left * base;
            x /= 10;
            base /= 100;
        }
        return true;
    }
}
</code></pre>