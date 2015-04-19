---
layout: post
title: LeetCode 151 - Reverse Words in a String - 题解/Solution 
categories: Leetcode
tags: leetcode java
keywords: leetcode,java,solution,题解,解题报告
tagline: Supporting tagline
---
***<https://leetcode.com/problems/reverse-words-in-a-string/>***
<pre><code>/**
 * Given an input string, reverse the string word by word.
 * 
 * For example, Given s = "the sky is blue", return "blue is sky the".
 * 
 * Update (2015-02-12): For C programmers: Try to solve it in-place in O(1)
 * space.
 * 
 * click to show clarification. Clarification:
 * 
 * What constitutes a word?
 * A sequence of non-space characters constitutes a word.
 * 
 * Could the input string contain leading or trailing spaces?
 * Yes. However, your reversed string should not contain leading or trailing spaces.
 * 
 * How about multiple spaces between two words?
 * Reduce them to a single space in the reversed string.
 * 
 * @author dongyuxi
 *
 */
public class Solution {
    public String reverseWords(String s) {
        if (null == s) {
            return null;
        }

        String[] array = s.split(" ");
        StringBuilder sb = new StringBuilder();
        for (int i = array.length - 1; i >= 0; i--) {
            if (!"".equals(array[i])) {
                if (!"".equals(sb.toString())) {
                    sb.append(" ");
                }
                sb.append(array[i]);
            }
        }

        return sb.toString();
    }
}
</code></pre>