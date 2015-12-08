---
layout: post
title: LeetCode 168 - Excel Sheet Column Title - 题解/Solution 
categories: 刷题
tags: leetcode java
keywords: leetcode,java,solution,题解,解题报告
tagline: Supporting tagline
---
***<https://leetcode.com/problems/excel-sheet-column-title/>***
<pre><code>/**
 * Given a positive integer, return its corresponding column title as appear in
 * an Excel sheet.
 * 
 * For example:
 *  1 -> A
 *  2 -> B
 *  3 -> C
 *  ...
 *  26 -> Z
 *  27 -> AA
 *  28 -> AB 
 * 
 * @author dongyuxi
 *
 */
public class Solution {
    public String convertToTitle(int n) {
        if (n <= 0) {
            return null;
        }
        StringBuilder sb = new StringBuilder();
        while (n > 0) {
            sb.append((char)((n - 1) % 26 + 'A'));
            n = (n - 1) / 26;
        }
        return sb.reverse().toString();
    }
}
</code></pre>
