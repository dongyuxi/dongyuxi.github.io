---
layout: post
title: LeetCode 031 - Next Permutation - 题解/Solution 
categories: 刷题
tags: leetcode java
keywords: leetcode,java,solution,题解,解题报告
tagline: Supporting tagline
---
***<https://leetcode.com/problems/next-permutation/>***
<pre><code>/**
 * Implement next permutation, which rearranges numbers into the
 * lexicographically next greater permutation of numbers.
 * 
 * If such arrangement is not possible, it must rearrange it as the lowest
 * possible order (ie, sorted in ascending order).
 * 
 * The replacement must be in-place, do not allocate extra memory.
 * 
 * Here are some examples. Inputs are in the left-hand column and its
 * corresponding outputs are in the right-hand column.
 * 1,2,3 -> 1,3,2
 * 3,2,1 -> 1,2,3
 * 1,1,5 -> 1,5,1
 * 
 * @author dongyuxi
 *
 */
public class Solution {
    public void nextPermutation(int[] num) {
        if (null == num || num.length <= 1) {
            return;
        }

        int j = num.length - 1;
        while (j >= 1) {
            if (num[j - 1] < num[j]) {
                int minIndex = findMinIndex(num, j, num.length - 1, num[j - 1]);
                swap(num, j - 1, minIndex);
                break;
            }
            j--;
        }
        Arrays.sort(num, j, num.length);
    }

    private int findMinIndex(int[] num, int start, int end, int low) {
        int min = num[start];
        int minIndex = start;
        for (int i = start + 1; i <= end; i++) {
            if (num[i] < min && num[i] > low) {
                min = num[i];
                minIndex = i;
            }
        }
        return minIndex;
    }

    private void swap(int[] num, int i, int j) {
        int temp = num[i];
        num[i] = num[j];
        num[j] = temp;
    }
}
</code></pre>
