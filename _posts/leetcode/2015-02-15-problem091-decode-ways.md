---
layout: post
title: LeetCode 091 - Decode Ways - 题解/Solution 
categories: 刷题
tags: leetcode java
keywords: leetcode,java,solution,题解,解题报告
tagline: Supporting tagline
---
***<https://leetcode.com/problems/decode-ways/>***
<pre><code>/**
 * A message containing letters from A-Z is being encoded to numbers using the
 * following mapping:
 * 
 * 'A' -> 1
 * 'B' -> 2
 * ...
 * 'Z' -> 26
 * 
 * Given an encoded message containing digits, determine the total number of
 * ways to decode it.
 * 
 * For example, Given encoded message "12", it could be decoded as "AB" (1 2) or
 * "L" (12).
 * 
 * The number of ways decoding "12" is 2.
 * 
 * @author dongyuxi
 *
 */
public class Solution {
    public int numDecodings(String s) {
        if (null == s || 0 == s.length()) {
            return 0;
        }

        int[] dp = new int[s.length()];
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) < '0' || s.charAt(i) > '9') {
                return 0;
            }
            if (s.charAt(i) == '0') {
                if (i == 0 || s.charAt(i - 1) == '0' || s.charAt(i - 1) > '2') {
                    return 0;
                }
                dp[i] = (i == 1) ? 1 : dp[i - 2];
            } else {
                if (i > 0 && (s.charAt(i - 1) == '1' || (s.charAt(i - 1) == '2' && s.charAt(i) <= '6'))) {
                    dp[i] = ((i > 0) ? dp[i - 1] : 1) + ((i > 1) ? dp[i - 2] : 1);
                } else {
                    dp[i] = (i > 0) ? dp[i - 1] : 1;
                }
            }
        }

        return dp[s.length() - 1];
    }
}
</code></pre>
