---
layout: post
title: LeetCode 028 - Implement strStr() - 题解/Solution 
categories: 刷题
tags: [leetcode,java]
keywords: leetcode,java,solution,题解,解题报告
date: 2015-02-15
permalink: problem028-implement-strstr
---
***<https://leetcode.com/problems/implement-strstr/>***
<!--more-->
```java
/**
 * Implement strStr().
 * 
 * Returns the index of the first occurrence of needle in haystack, or -1 if
 * needle is not part of haystack.
 * 
 * @author dongyuxi
 *
 */
public class Solution {
    public int strStr(String haystack, String needle) {
        return haystack.indexOf(needle);
    }
}
```