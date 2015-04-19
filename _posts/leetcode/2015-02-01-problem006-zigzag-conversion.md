---
layout: post
title: LeetCode 006 - ZigZag Conversion - 题解/Solution
categories: Leetcode
tags: leetcode java
keywords: leetcode,java,solution,题解,解题报告
tagline: Supporting tagline
---
***<https://leetcode.com/problems/zigzag-conversion/>***
<pre><code>/**
 *  The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
 *  (you may want to display this pattern in a fixed font for better legibility)
 *  P   A   H   N
 *  A P L S I I G
 *  Y   I   R
 *  And then read line by line: "PAHNAPLSIIGYIR"
 *  Write the code that will take a string and make this conversion given a number of rows:
 *  string convert(string text, int nRows);
 *  convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR". 
 * 
 * @author dongyuxi
 *
 */
public class Solution {
    public String convert(String s, int nRows) {
        if (s == null || s.length() <= nRows || nRows <= 1)
            return s;

        StringBuffer sb = new StringBuffer();
        for (int i = 0; i < s.length(); i += (nRows - 1) * 2) {
            sb.append(s.charAt(i));
        }

        for (int i = 1; i < nRows - 1; i++) {
            for (int j = i; j < s.length(); j += (nRows - 1) * 2) {
                sb.append(s.charAt(j));
                if (j + (nRows - i - 1) * 2 < s.length()) {
                    sb.append(s.charAt(j + (nRows - i - 1) * 2));
                }
            }
        }
        for (int i = nRows - 1; i < s.length(); i += (nRows - 1) * 2) {
            sb.append(s.charAt(i));
        }

        return sb.toString();
    }
}
</code></pre>