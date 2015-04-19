---
layout: post
title: LeetCode 171 - Excel Sheet Column Number - 题解/Solution 
categories: Leetcode
tags: leetcode java
keywords: leetcode,java,solution,题解,解题报告
tagline: Supporting tagline
---
***<https://leetcode.com/problems/excel-sheet-column-number/>***
<pre><code>/**
 * Related to question Excel Sheet Column Title

 * Given a column title as appear in an Excel sheet, return its corresponding column number.
 * 
 * For example:
 *  A -> 1
 *  B -> 2
 *  C -> 3
 *  ...
 *  Z -> 26
 *  AA -> 27
 *  AB -> 28
 * 
 * @author dongyuxi
 *
 */
public class Solution {
    public int titleToNumber(String s) {
        if (null == s || 0 == s.length()) {
            return 0;
        }

        int total = 0;
        for (int i = 0; i < s.length(); i++) {
            if (!(s.charAt(i) >= 'A' && s.charAt(i) <= 'Z')) {
                return 0;
            }
            total = total * 26 + s.charAt(i) - 'A' + 1;
        }
        return total;
    }
}
</code></pre>