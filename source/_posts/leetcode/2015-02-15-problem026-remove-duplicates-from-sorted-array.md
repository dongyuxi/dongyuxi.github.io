---
layout: post
title: LeetCode 026 - Remove Duplicates from Sorted Array - 题解/Solution 
categories: 刷题
tags: [leetcode,java]
keywords: leetcode,java,solution,题解,解题报告
date: 2015-02-15
permalink: problem026-remove-duplicates-from-sorted-array
---
***<https://leetcode.com/problems/remove-duplicates-from-sorted-array/>***
<!--more-->
```java
/**
 * Given a sorted array, remove the duplicates in place such that each element
 * appear only once and return the new length.
 * 
 * Do not allocate extra space for another array, you must do this in place with
 * constant memory.
 * 
 * For example, Given input array A = [1,1,2],
 * 
 * Your function should return length = 2, and A is now [1,2].
 * 
 * @author dongyuxi
 *
 */
public class Solution {
    public int removeDuplicates(int[] A) {
        if (null == A || 0 == A.length) {
            return 0;
        }

        int scanIndex = 0;

        for (int i = 0; i < A.length; i++) {
            if (A[i] == A[scanIndex]) {
                continue;
            }
            A[++scanIndex] = A[i];
        }

        return scanIndex + 1;
    }
}
```