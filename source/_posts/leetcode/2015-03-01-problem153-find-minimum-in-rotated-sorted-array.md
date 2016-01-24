---
layout: post
title: LeetCode 153 - Find Minimum in Rotated Sorted Array - 题解/Solution 
categories: 刷题
tags: [leetcode,java]
keywords: leetcode,java,solution,题解,解题报告
date: 2015-03-01
permalink: problem153-find-minimum-in-rotated-sorted-array
---
***<https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/>***
<!--more-->
```java
/**
 * Suppose a sorted array is rotated at some pivot unknown to you beforehand.
 * 
 * (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
 * 
 * Find the minimum element.
 * 
 * You may assume no duplicate exists in the array.
 * 
 * @author dongyuxi
 *
 */
public class Solution {
    public int findMin(int[] num) {
        if (null == num || 0 == num.length) {
            return -1;
        }
        return binFindMin(num, 0, num.length - 1);
    }

    private int binFindMin(int[] num, int start, int end) {
        if (num[start] <= num[end]) {
            return num[start];
        }
        int mid = (start + end) / 2;
        if (num[start] <= num[mid]) {
            return binFindMin(num, mid + 1, end);
        } else {
            return binFindMin(num, start, mid);
        }
    }
}
```