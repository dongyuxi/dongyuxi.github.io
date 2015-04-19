---
layout: post
title: LeetCode 010 - Regular Expression Matching  - 题解/Solution
categories: Leetcode
tags: leetcode java
keywords: leetcode,java,solution,题解,解题报告
tagline: Supporting tagline
---
***<https://leetcode.com/problems/regular-expression-matching/>***
<pre><code>/**
 * Implement regular expression matching with support for '.' and '*'.
 * 
 * '.' Matches any single character.
'*' Matches zero or more of the preceding element.
 * 
 * @author dongyuxi
 *
 */
public class Solution {
    public boolean isMatch(String s, String p) {
        if (null == s && null == p) {
            return true;
        }
        if (null == p) {
            return false;
        }
        if (0 == p.length()) {
            return 0 == s.length();
        }

        if (1 == p.length()) {
            if (1 == s.length() && (s.charAt(0) == p.charAt(0) || '.' == p.charAt(0))) {
                return true;
            }
            return false;
        }

        if ('*' == p.charAt(1)) {
            while (s.length() > 0 && (s.charAt(0) == p.charAt(0) || '.' == p.charAt(0))) {
                if (isMatch(s, p.substring(2))) {
                    return true;
                }
                s = s.substring(1);
            }
            return isMatch(s, p.substring(2));
        } else {
            if (s.length() > 0 && (s.charAt(0) == p.charAt(0) || '.' == p.charAt(0))) {
                return isMatch(s.substring(1), p.substring(1));
            }
            return false;
        }
    }
}
</code></pre>