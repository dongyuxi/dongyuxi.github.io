---
layout: post
title: LeetCode 080 - Remove Duplicates from Sorted Array II - 题解/Solution 
categories: Leetcode
tags: leetcode java
keywords: leetcode,java,solution,题解,解题报告
tagline: Supporting tagline
---
***<https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/>***
<pre><code>/**
 * Follow up for "Remove Duplicates": What if duplicates are allowed at most
 * twice?
 * 
 * For example, Given sorted array A = [1,1,1,2,2,3],
 * 
 * Your function should return length = 5, and A is now [1,1,2,2,3].
 * 
 * @author dongyuxi
 *
 */
public class Solution {
    public int removeDuplicates(int[] A) {
        if (null == A || 0 == A.length) {
            return 0;
        }

        int scanIndex = 0;
        int count = 1;

        for (int i = 1; i < A.length; i++) {
            if (A[i] == A[scanIndex]) {
                if (2 == count) {
                    continue;
                }
                count++;
                A[++scanIndex] = A[i];
            } else {
                A[++scanIndex] = A[i];
                count = 1;
            }
        }

        return scanIndex + 1;
    }
}
</code></pre>