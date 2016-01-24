---
layout: post
title: LeetCode 088 - Merge Sorted Array - 题解/Solution 
categories: 刷题
tags: [leetcode,java]
keywords: leetcode,java,solution,题解,解题报告
date: 2015-02-15
permalink: problem088-merge-sorted-array
---
***<https://leetcode.com/problems/merge-sorted-array/>***
<!--more-->
```java
/**
 * Given two sorted integer arrays A and B, merge B into A as one sorted array.
 * 
 * Note: You may assume that A has enough space (size that is greater or equal
 * to m + n) to hold additional elements from B. The number of elements
 * initialized in A and B are m and n respectively.
 * 
 * @author dongyuxi
 *
 */
public class Solution {
    public void merge(int A[], int m, int B[], int n) {
        int index = m + n - 1;
        while (m > 0 && n > 0) {
            if (A[m - 1] >= B[n - 1]) {
                A[index--] = A[m - 1];
                m--;
            } else {
                A[index--] = B[n - 1];
                n--;
            }
        }
        while (m > 0) {
                A[index--] = A[m - 1];
                m--;
        }
        while (n > 0) {
            A[index--] = B[n - 1];
            n--;
    }
    }
}
```