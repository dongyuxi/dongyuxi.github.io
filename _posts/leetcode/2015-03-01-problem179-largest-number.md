---
layout: post
title: LeetCode 179 - Largest Number - 题解/Solution 
categories: Leetcode
tags: leetcode java
keywords: leetcode,java,solution,题解,解题报告
tagline: Supporting tagline
---
***<https://leetcode.com/problems/largest-number/>***
<pre><code>/**
 * Given a list of non negative integers, arrange them such that they form the
 * largest number.
 * 
 * For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.
 * 
 * Note: The result may be very large, so you need to return a string instead of
 * an integer.
 * 
 * @author dongyuxi
 *
 */
public class Solution {
    public String largestNumber(int[] num) {
        if (null == num) {
            return "";
        }

        qsort(num, 0, num.length - 1);
        if (num[num.length - 1] == 0) {
            return "0";
        }

        StringBuilder sb = new StringBuilder();
        for (int i = num.length - 1; i >= 0; i--) {
            sb.append(num[i]);
        }

        return sb.toString();
    }

    private void qsort(int[] num, int low, int high) {
        if (low < high) {
            int mid = partition(num, low, high);
            qsort(num, low, mid - 1);
            qsort(num, mid + 1, high);
        }
    }

    private int partition(int[] num, int low, int high) {
        if (low < high) {
            int val = num[low];
            while (low < high) {
                while (low < high && cmp(num[high], val) > 0 ) {
                    high--;
                }
                num[low] = num[high];
                while (low < high && cmp(num[low], val) <= 0) {
                    low++;
                }
                num[high] = num[low];
            }
            num[low] = val;
            return low;
        }

        return -1;
    }

    private int cmp(int a, int b) {
        String ab = Integer.toString(a) + Integer.toString(b);
        String ba = Integer.toString(b) + Integer.toString(a);
        return ab.compareTo(ba);
    }
}
</code></pre>