---
layout: post
title: LeetCode 016 - 3Sum Closest - 题解/Solution
categories: 刷题
tags: [leetcode,java]
keywords: leetcode,java,solution,题解,解题报告
date: 2015-02-08
permalink: problem016-3sum-closest
---
***<https://leetcode.com/problems/3sum-closest/>***
<!--more-->
```java
/**
 * Given an array S of n integers, find three integers in S such that the sum is
 * closest to a given number, target. Return the sum of the three integers. You
 * may assume that each input would have exactly one solution.
 * 
 * For example, given array S = {-1 2 1 -4}, and target = 1.
 * 
 * The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
 * 
 * 
 * @author dongyuxi
 *
 */
public class Solution {
    public int threeSumClosest(int[] num, int target) {
        if (null == num || num.length < 3) {
            return 0;
        }

        Arrays.sort(num);
        int diff = Integer.MAX_VALUE;
        int closest = 0;
        for (int i = 0; i < num.length - 2; i++) {
            if (i > 0 && num[i] == num[i - 1]) {
                continue;
            }
            int j = i + 1;
            int k = num.length - 1;
            while (j < k) {
                if (j > i + 1 && num[j] == num[j - 1]) {
                    j++;
                    continue;
                }
                if (k < num.length - 1 && num[k] == num[k + 1]) {
                    k--;
                    continue;
                }
                int sum = num[i] + num[j] + num[k];
                if (sum < target) {
                    if (Math.abs(sum - target) < diff) {
                        diff = Math.abs(sum - target);
                        closest = sum;
                    }
                    j++;
                } else if (sum > target) {
                    if (Math.abs(sum - target) < diff) {
                        diff = Math.abs(sum - target);
                        closest = sum;
                    }
                    k--;
                } else {
                    return target;
                }
            }
        }

        return closest;
    }
}
```