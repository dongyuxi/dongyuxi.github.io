---
layout: post
title: LeetCode 038 - Count and Say - 题解/Solution 
categories: Leetcode
tags: leetcode java
keywords: leetcode,java,solution,题解,解题报告
tagline: Supporting tagline
---
***<https://leetcode.com/problems/count-and-say/>***
<pre><code>/**
 * The count-and-say sequence is the sequence of integers beginning as follows:
 * 1, 11, 21, 1211, 111221, ...
 * 
 * 1 is read off as "one 1" or 11.
 * 11 is read off as "two 1s" or 21.
 * 21 is read off as "one 2, then one 1" or 1211.
 * 
 * Given an integer n, generate the nth sequence.
 * 
 * Note: The sequence of integers will be represented as a string.
 * 
 * @author dongyuxi
 *
 */
public class Solution {
    public String countAndSay(int n) {
        if (n <= 0) {
            return "";
        }

        StringBuilder sb = new StringBuilder("1");
        for (int i = 1; i < n; i++) {
            sb = nextSequence(sb);
        }

        return sb.toString();
    }

    private StringBuilder nextSequence(StringBuilder sb) {
        if (null == sb || 0 == sb.length()) {
            return new StringBuilder();
        }

        StringBuilder newSb = new StringBuilder();
        char last = sb.charAt(0);
        int count = 1;
        for (int i = 1; i < sb.length(); i++) {
            if (sb.charAt(i) == last) {
                count++;
            } else {
                newSb.append(count).append(last);
                last = sb.charAt(i);
                count = 1;
            }
        }
        newSb.append(count).append(last);

        return newSb;
    }
}
</code></pre>