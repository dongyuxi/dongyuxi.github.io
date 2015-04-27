---
layout: post
title: LeetCode 045 - Jump Game II - 题解/Solution
categories: Leetcode
tags: leetcode java
keywords: leetcode,java,solution,题解,解题报告
tagline: Supporting tagline
---
***<https://leetcode.com/problems/jump-game-ii/>***
<pre><code>/**
 * Given an array of non-negative integers, you are initially positioned at the
 * first index of the array.
 * 
 * Each element in the array represents your maximum jump length at that
 * position.
 * 
 * Your goal is to reach the last index in the minimum number of jumps.
 * 
 * For example: Given array A = [2,3,1,1,4]
 * 
 * The minimum number of jumps to reach the last index is 2. (Jump 1 step from
 * index 0 to 1, then 3 steps to the last index.)
 * 
 * @author dongyuxi
 *
 */
public class Solution {
    public int jump(int[] nums) {
        if (null == nums || 0 == nums.length) {
            return -1;
        }
        int step = 0;
        int curJump = 0;
        int maxJump = 0;
        for (int i = 0; i < nums.length; i++) {
            if (curJump < i) {
                step++;
                curJump = maxJump;
            }
            maxJump = Math.max(maxJump, nums[i] + i);
        }
        return step;
    }
}
</code></pre>
