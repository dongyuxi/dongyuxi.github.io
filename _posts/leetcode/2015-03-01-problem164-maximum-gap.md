---
layout: post
title: LeetCode 164 - Maximum Gap - 题解/Solution 
categories: 刷题
tags: leetcode java
keywords: leetcode,java,solution,题解,解题报告
tagline: Supporting tagline
---
***<https://leetcode.com/problems/maximum-gap/>***
<pre><code>/**
 * Given an unsorted array, find the maximum difference between the successive
 * elements in its sorted form.
 * 
 * Try to solve it in linear time/space.
 * 
 * Return 0 if the array contains less than 2 elements.
 * 
 * You may assume all elements in the array are non-negative integers and fit in
 * the 32-bit signed integer range.
 * 
 * @author dongyuxi
 *
 */
public class Solution {
    public int maximumGap(int[] num) {
        if (null == num || num.length < 2) {
            return 0;
        }
        if (2 == num.length) {
            return Math.abs(num[0] - num[1]);
        }

        int max = Integer.MIN_VALUE;
        int min = Integer.MAX_VALUE;
        for (int i = 0; i < num.length; i++) {
            if (num[i] > max) {
                max = num[i];
            }
            if (num[i] < min) {
                min = num[i];
            }
        }

        int gap = (int)(Math.ceil((max - min) / (num.length - 1)) + 1);
        int bucketCount = (max - min) / gap + 1;
        int[] bucketMax = new int[bucketCount];
        int[] bucketMin = new int[bucketCount];
        boolean[] bucketNoEmpty = new boolean[bucketCount];
        for (int i = 0; i < num.length; i++) {
            int index = (num[i] - min) / gap;
            if (!bucketNoEmpty[index]) {
                bucketMax[index] = num[i];
                bucketMin[index] = num[i];
                bucketNoEmpty[index] = true;
            } else {
                if (num[i] < bucketMin[index]) {
                    bucketMin[index] = num[i];
                }
                if (num[i] > bucketMax[index]) {
                    bucketMax[index] = num[i];
                }
            }
        }

        int maxGap = 0;
        int previous = 0;
        for (int i = 1; i < bucketCount; i++) {
            if (bucketNoEmpty[i]) {
                maxGap = Math.max(maxGap, bucketMin[i] - bucketMax[previous]);
                previous = i;
            }
        }

        return maxGap;
    }
}
</code></pre>
