---
layout: post
title: LeetCode 005 - Longest Palindromic Substring - 题解/Solution
categories: 刷题
tags: leetcode java
keywords: leetcode,java,solution,题解,解题报告
tagline: Supporting tagline
---
***<https://leetcode.com/problems/longest-palindromic-substring/>***
<pre><code>/**
 * Given a string S, find the longest palindromic substring in S. You may assume
 * that the maximum length of S is 1000, and there exists one unique longest
 * palindromic substring.
 * 
 * @author dongyuxi
 *
 */
public class Solution {
    public String longestPalindrome(String s) {
        if (null == s || 0 == s.length()) {
            return s;
        }

        int longest = 0;
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < s.length(); i++) {
            int left = i - 0;
            int right = s.length() - 1 - i;
            int min = Math.min(left, right);
            int j = 0;
            while (j < min) {
                if (s.charAt(i - j - 1) != s.charAt(i + j + 1)) {
                    break;
                }
                j++;
            }

            if (2 * j + 1 > longest) {
                longest = 2 * j + 1;
                sb.delete(0, sb.length());
                sb.append(s.substring(i - j, i + j + 1));
            }

            if (i < s.length() - 1 && s.charAt(i) == s.charAt(i + 1)) {
                right = s.length() - 2 - i;
                min = Math.min(left, right);
                j = 0;
                while (j < min) {
                    if (s.charAt(i - j - 1) != s.charAt(i + j + 2)) {
                        break;
                    }
                    j++;
                }
                if (2 * j + 2 > longest) {
                    longest = 2 * j + 2;
                    sb.delete(0, sb.length());
                    sb.append(s.substring(i - j, i + j + 2));
                }
            }
        }

        return sb.toString();
    }
}
</code></pre>
