---
layout: post
title: LeetCode 055 - Jump Game - 题解/Solution
categories: Leetcode
tags: leetcode java
keywords: leetcode,java,solution,题解,解题报告
tagline: Supporting tagline
---
***<https://leetcode.com/problems/jump-game/>***
<pre><code>/**
 * Given an array of non-negative integers, you are initially positioned at the
 * first index of the array.
 * 
 * Each element in the array represents your maximum jump length at that
 * position.
 * 
 * Determine if you are able to reach the last index.
 * 
 * For example: A = [2,3,1,1,4], return true.
 * 
 * A = [3,2,1,0,4], return false.
 * 
 * @author dongyuxi
 *
 */
public class Solution {
    public boolean canJump(int[] nums) {
        if (null == nums || 0 == nums.length) {
            return false;
        }
        int maxJump = nums[0];
        for (int i = 1; i < nums.length; i++) {
            if (maxJump > 0) {
                maxJump--;
                maxJump = Math.max(maxJump, nums[i]);
            } else {
                return false;
            }
        }
        return true;
    }
}
</code></pre>
