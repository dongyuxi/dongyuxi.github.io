---
layout: post
title: LeetCode 039 - Combination Sum - 题解/Solution 
categories: Leetcode
tags: leetcode java
keywords: leetcode,java,solution,题解,解题报告
tagline: Supporting tagline
---
***<https://leetcode.com/problems/combination-sum/>***
<pre><code>/**
 * Given a set of candidate numbers (C) and a target number (T), find all unique
 * combinations in C where the candidate numbers sums to T.
 * 
 * The same repeated number may be chosen from C unlimited number of times.
 * 
 * Note:
 * 
 * All numbers (including target) will be positive integers. Elements in a
 * combination (a1, a2, ... , ak) must be in non-descending order. (ie, a1 <= a2 <=
 * ... <= ak). The solution set must not contain duplicate combinations.
 * 
 * For example, given candidate set 2,3,6,7 and target 7, A solution set is: [7]
 * [2, 2, 3]
 * 
 * @author dongyuxi
 *
 */
public class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> listlist = new ArrayList<List<Integer>>();
        List<Integer> list = new ArrayList<Integer>();
        if (null == candidates || 0 == candidates.length) {
            listlist.add(list);
            return listlist;
        }

        Arrays.sort(candidates);
        combinationSum(candidates, target, 0, list, listlist);
        return listlist;
    }

    private void combinationSum(int[] candidates, int target, int index,
            List<Integer> list, List<List<Integer>> listlist) {
        if (target < 0) {
            return;
        }
        if (index == candidates.length) {
            if (0 == target) {
                listlist.add(new ArrayList<Integer>(list));
            }
            return;
        }

        for (int i = 0; i <= target / candidates[index]; i++) {
            for (int j = 0; j < i; j++) {
                list.add(candidates[index]);
            }
            combinationSum(candidates, target - i * candidates[index], index + 1, list, listlist);
            for (int j = 0; j < i; j++) {
                list.remove(list.size() - 1);
            }
        }
    }
}
</code></pre>