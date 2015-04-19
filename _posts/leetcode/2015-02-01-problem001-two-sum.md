---
layout: post
title: LeetCode 001 - Two Sum - 题解/solution 
categories: Leetcode
tags: leetcode java
keywords: leetcode,java,solution,题解,解题报告
tagline: Supporting tagline
---
***<https://leetcode.com/problems/two-sum/>***
<pre><code>/**
 * Given an array of integers, find two numbers such that they add up to a
 * specific target number.
 * 
 * The function twoSum should return indices of the two numbers such that they
 * add up to the target, where index1 must be less than index2. Please note that
 * your returned answers (both index1 and index2) are not zero-based.
 * 
 * You may assume that each input would have exactly one solution.
 * 
 * @Input: numbers={2, 7, 11, 15}, target=9 
 * @Output: index1=1, index2=2
 * 
 * @author dongyuxi
 *
 */
public class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int[] index = new int[2];
        Map<Integer, Integer> targetNumberIndexMap = new HashMap<Integer, Integer>();
        for (int i = 0; i < numbers.length; i++) {
            targetNumberIndexMap.put(target - numbers[i], i);
        }
        for (int i = 0; i < numbers.length; i++) {
            if (targetNumberIndexMap.containsKey(numbers[i])) {
                int targetIndex = targetNumberIndexMap.get(numbers[i]);
                if (targetIndex != i) {
                    index[0] = Integer.min(targetIndex, i) + 1;
                    index[1] = Integer.max(targetIndex, i) + 1;
                }
            }
        }
        return index;
    }
}

</code></pre>