---
layout: post
title: LeetCode 058 - Length of Last Word - 题解/Solution 
categories: 刷题
tags: [leetcode,java]
keywords: leetcode,java,solution,题解,解题报告
date: 2015-02-15
permalink: problem058-length-of-last-word
---
***<https://leetcode.com/problems/length-of-last-word/>***
<!--more-->
```java
/**
 * Given a string s consists of upper/lower-case alphabets and empty space
 * characters ' ', return the length of last word in the string.
 * 
 * If the last word does not exist, return 0.
 * 
 * Note: A word is defined as a character sequence consists of non-space
 * characters only.
 * 
 * For example, Given s = "Hello World", return 5.
 * 
 * @author dongyuxi
 *
 */
public class Solution {
    public int lengthOfLastWord(String s) {
        if (null == s) {
            return 0;
        }

        int length = 0;
        int index = s.length() - 1;
        boolean start = false;
        while (index >= 0) {
            if (s.charAt(index) != ' ' && s.charAt(index) != '\t') {
                if (!start) {
                    start = true;
                }
                length++;
            } else {
                if (start) {
                    return length;
                }
            }
            index--;
        }

        if (!start) {
            return 0;
        }

        return length;
    }
}
```