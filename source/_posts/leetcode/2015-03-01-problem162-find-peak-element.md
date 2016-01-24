---
layout: post
title: LeetCode 162 - Find Peak Element - 题解/Solution 
categories: 刷题
tags: [leetcode,java]
keywords: leetcode,java,solution,题解,解题报告
date: 2015-03-01
permalink: problem162-find-peak-element
---
***<https://leetcode.com/problems/find-peak-element/>***
<!--more-->
```java
/**
 * A peak element is an element that is greater than its neighbors.
 * 
 * Given an input array where num[i] ≠ num[i+1], find a peak element and return
 * its index.
 * 
 * The array may contain multiple peaks, in that case return the index to any
 * one of the peaks is fine.
 * 
 * You may imagine that num[-1] = num[n] = -∞.
 * 
 * For example, in array [1, 2, 3, 1], 3 is a peak element and your function
 * should return the index number 2.
 * 
 * Note: Your solution should be in logarithmic complexity.
 * 
 * @author dongyuxi
 *
 */
public class Solution {
    public int findPeakElement(int[] num) {
        if (null == num || 0 == num.length) {
            return 0;
        }

        int low = 0;
        int high = num.length - 1;
        while (low <= high) {
            if (low == high) {
                return low;
            }
            int mid = low + (high - low) / 2;
            if (num[mid] > num[mid + 1]) {
                high = mid;
            } else {
                low = mid + 1;
            }
        }

        return high;
    }
}
```