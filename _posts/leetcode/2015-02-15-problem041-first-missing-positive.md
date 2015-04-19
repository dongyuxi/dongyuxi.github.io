---
layout: post
title: LeetCode 041 - First Missing Positive - 题解/Solution 
categories: Leetcode
tags: leetcode java
keywords: leetcode,java,solution,题解,解题报告
tagline: Supporting tagline
---
***<https://leetcode.com/problems/first-missing-positive/>***
<pre><code>/**
 * Given an unsorted integer array, find the first missing positive integer.
 * 
 * For example, Given [1,2,0] return 3, and [3,4,-1,1] return 2.
 * 
 * Your algorithm should run in O(n) time and uses constant space.
 * 
 * @author dongyuxi
 *
 */
public class Solution {
    public int firstMissingPositive(int[] A) {
        if (null == A || 0 == A.length) {
            return 1;
        }

        for (int i = 0; i < A.length; i++) {
            A[i] = A[i] - 1;
        }

        for (int i = 0; i < A.length; i++) {
            while (A[i] >= 0 && A[i] < A.length && A[i] != i && A[i] != A[A[i]]) {
                swap(A, i, A[i]);
            }
        }

        int result = A.length + 1;
        for (int i = 0; i < A.length; i++) {
            if (A[i] != i) {
                result = i + 1;
                break;
            }
        }

        return result;
    }

    private void swap(int[] a, int i, int j) {
        int temp = a[i];
        a[i] = a[j];
        a[j] = temp;
    }
}
</code></pre>