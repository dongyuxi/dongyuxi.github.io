---
layout: post
title: LeetCode 125 - Valid Palindrome - 题解/Solution 
categories: 刷题
tags: leetcode java
keywords: leetcode,java,solution,题解,解题报告
tagline: Supporting tagline
---
***<https://leetcode.com/problems/valid-palindrome/>***
<pre><code>/**
 * Given a string, determine if it is a palindrome, considering only
 * alphanumeric characters and ignoring cases.
 * 
 * For example, "A man, a plan, a canal: Panama" is a palindrome. "race a car"
 * is not a palindrome.
 * 
 * Note: Have you consider that the string might be empty? This is a good
 * question to ask during an interview.
 * 
 * For the purpose of this problem, we define empty string as valid palindrome.
 * 
 * @author dongyuxi
 *
 */
public class Solution {
    public boolean isPalindrome(String s) {
        if (null == s) {
            return true;
        }

        int low = 0;
        int high = s.length() - 1;
        while (low < high) {
            while (low < high && !(Character.isLetterOrDigit(s.charAt(low)))) {
                low++;
            }
            while (low < high && !(Character.isLetterOrDigit(s.charAt(high)))) {
                high--;
            }
            if (Character.toLowerCase(s.charAt(low)) != (Character.toLowerCase(s.charAt(high)))) {
                return false;
            }
            low++;
            high--;
        }

        return true;
    }
}
</code></pre>
