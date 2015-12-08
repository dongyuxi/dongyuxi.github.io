---
layout: post
title: LeetCode 035 - Search Insert Position - 题解/Solution 
categories: 刷题
tags: leetcode java
keywords: leetcode,java,solution,题解,解题报告
tagline: Supporting tagline
---
***<https://leetcode.com/problems/search-insert-position/>***
<pre><code>/**
 * Given a sorted array and a target value, return the index if the target is
 * found. If not, return the index where it would be if it were inserted in
 * order.
 * 
 * You may assume no duplicates in the array.
 * 
 * Here are few examples.
 * [1,3,5,6], 5 -> 2
 * [1,3,5,6], 2 -> 1
 * [1,3,5,6], 7 -> 4
 * [1,3,5,6], 0 -> 0
 * 
 * @author dongyuxi
 *
 */
public class Solution {
    public int searchInsert(int[] A, int target) {
        if (null == A || 0 == A.length) {
            return -1;
        }

        return binSearch(A, 0, A.length - 1, target);
    }

    private int binSearch(int[] a, int start, int end, int target) {
        while (start <= end) {
            int mid = (start + end) / 2;
            if (a[mid] == target) {
                return mid;
            }
            if (target < a[mid]) {
                end = mid - 1;
            } else if (a[mid] < target) {
                start = mid + 1;
            }
        }
        return start;
    }

}
</code></pre>
