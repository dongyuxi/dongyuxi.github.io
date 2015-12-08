---
layout: post
title: LeetCode 189 - Rotate Array - 题解/Solution 
categories: 刷题
tags: leetcode java
keywords: leetcode,java,solution,题解,解题报告
tagline: Supporting tagline
---
***<https://leetcode.com/problems/rotate-array/>***
<pre><code>/**
 * Rotate an array of n elements to the right by k steps.
 * 
 * For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to
 * [5,6,7,1,2,3,4].
 * 
 * Note: Try to come up as many solutions as you can, there are at least 3
 * different ways to solve this problem.
 * 
 * @author dongyuxi
 *
 */
public class Solution {
    public void rotate(int[] nums, int k) {
        if (null == nums) {
            return;
        }

        int length = nums.length;
        if (k < 0) {
            k = length - (-k) % length;
        } else {
            k = k % length;
        }
        reverse(nums, 0, length - k - 1);
        reverse(nums, length - k, length - 1);
        reverse(nums, 0, length - 1);
    }

    private void reverse(int[] nums, int start, int end) {
        while (start < end) {
            int temp = nums[start];
            nums[start] = nums[end];
            nums[end] = temp;
            start++;
            end--;
        }
    }
}
</code></pre>
