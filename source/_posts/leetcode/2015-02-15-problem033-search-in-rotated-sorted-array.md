---
layout: post
title: LeetCode 033 - Search in Rotated Sorted Array - 题解/Solution 
categories: 刷题
tags: [leetcode,java]
keywords: leetcode,java,solution,题解,解题报告
date: 2015-02-15
permalink: problem033-search-in-rotated-sorted-array
---
***<https://leetcode.com/problems/search-in-rotated-sorted-array/>***
<!--more-->
```java
/**
 * Suppose a sorted array is rotated at some pivot unknown to you beforehand.
 * 
 * (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
 * 
 * You are given a target value to search. If found in the array return its
 * index, otherwise return -1.
 * 
 * You may assume no duplicate exists in the array.
 * 
 * @author dongyuxi
 *
 */
public class Solution {
    public int search(int[] A, int target) {
        if (null == A || 0 == A.length) {
            return -1;
        }

        return rotatedBinSearch(A, 0, A.length - 1, target);
    }

    private int rotatedBinSearch(int[] A, int start, int end, int target) {
        if (start > end) {
            return -1;
        }
        
        int mid = (start + end) / 2;
        if (A[start] <= A[mid]) {
            if (A[start] <= target && target <= A[mid]) {
                return binSearch(A, start, mid, target);
            } else {
                return rotatedBinSearch(A, mid + 1, end, target);
            }
        } else {
            if (mid + 1 > end) {
                return -1;
            }
            if (A[mid + 1] <= target && target <= A[end]) {
                return binSearch(A, mid + 1, end, target);
            } else {
                return rotatedBinSearch(A, start, mid, target);
            }
        }
    }

    private int binSearch(int[] A, int start, int end, int target) {
        while (start <= end) {
            int mid = (start + end) / 2;
            if (target == A[mid]) {
                return mid;
            }
            if (target < A[mid]) {
                end = mid - 1;
                continue;
            }
            start = mid + 1;
        }
        return -1;
    }
}
```