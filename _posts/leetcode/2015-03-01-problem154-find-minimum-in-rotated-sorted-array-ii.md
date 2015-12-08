---
layout: post
title: LeetCode 154 - Find Minimum in Rotated Sorted Array II - 题解/Solution 
categories: 刷题
tags: leetcode java
keywords: leetcode,java,solution,题解,解题报告
tagline: Supporting tagline
---
***<https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/>***
<pre><code>/**
 * Follow up for "Find Minimum in Rotated Sorted Array": What if duplicates are
 * allowed?
 * 
 * Would this affect the run-time complexity? How and why? Suppose a sorted
 * array is rotated at some pivot unknown to you beforehand.
 * 
 * (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
 * 
 * Find the minimum element.
 * 
 * The array may contain duplicates.
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
        if (start == end || num[start] < num[end]) {
            return num[start];
        }

        int mid = (start + end) / 2;
        if (num[start] < num[mid]) {
            return binFindMin(num, mid + 1, end);
        } else if (num[start] > num[mid]) {
            return binFindMin(num, start, mid);
        } else {
            if (start == mid && num[start] > num[end]) {
                return num[end];
            }
            return binFindMin(num, start + 1, end);
        }
    }
}
</code></pre>
