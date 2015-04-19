---
layout: post
title: LeetCode 034 - Search for a Range - 题解/Solution 
categories: Leetcode
tags: leetcode java
keywords: leetcode,java,solution,题解,解题报告
tagline: Supporting tagline
---
***<https://leetcode.com/problems/search-for-a-range/>***
<pre><code>/**
 * Given a sorted array of integers, find the starting and ending position of a
 * given target value.
 * 
 * Your algorithm's runtime complexity must be in the order of O(log n).
 * 
 * If the target is not found in the array, return [-1, -1].
 * 
 * For example, Given [5, 7, 7, 8, 8, 10] and target value 8, return [3, 4].
 * 
 * @author dongyuxi
 *
 */
public class Solution {
    public int[] searchRange(int[] A, int target) {
        if (null == A || 0 == A.length) {
            return new int[]{-1, -1};
        }

        int minIndex = getMinIndex(A, 0, A.length - 1, target);
        int maxIndex = -1;
        if (-1 != minIndex) {
            maxIndex = getMaxIndex(A, 0, A.length - 1, target);
        }
        int[] index = new int[]{minIndex, maxIndex};

        return index;
    }

    private int getMinIndex(int[] a, int start, int end, int target) {
        while (start <= end) {
            int mid = (start + end) / 2;
            if (target < a[mid]) {
                end = mid - 1;
            } else if (target > a[mid]) {
                start = mid + 1;
            } else {
                if (start < mid && a[mid - 1] == target) {
                    end = mid - 1;
                } else {
                    return mid;
                }
            }
        }
        return -1;
    }

    private int getMaxIndex(int[] a, int start, int end, int target) {
        while (start <= end) {
            int mid = (start + end) / 2;
            if (target < a[mid]) {
                end = mid - 1;
            } else if (target > a[mid]) {
                start = mid + 1;
            } else {
                if (mid < end && a[mid + 1] == target) {
                    start = mid + 1;
                } else {
                    return mid;
                }
            }
        }
        return -1;
    }
}
</code></pre>