---
layout: post
title: LeetCode 040 - Combination Sum II - 题解/Solution 
categories: 刷题
tags: leetcode java
keywords: leetcode,java,solution,题解,解题报告
tagline: Supporting tagline
---
***<https://leetcode.com/problems/combination-sum-ii/>***
<pre><code>/**
 * Given a collection of candidate numbers (C) and a target number (T), find all
 * unique combinations in C where the candidate numbers sums to T.
 * 
 * Each number in C may only be used once in the combination.
 * 
 * Note:
 * 
 * All numbers (including target) will be positive integers. Elements in a
 * combination (a1, a2, ... , ak) must be in non-descending order. (ie, a1 <= a2 
 * <= ... <= ak). The solution set must not contain duplicate combinations.
 * 
 * For example, given candidate set 10,1,2,7,6,1,5 and target 8, A solution set
 * is: [1, 7] [1, 2, 5] [2, 6] [1, 1, 6]
 * 
 * @author dongyuxi
 *
 */
public class Solution {
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        List<List<Integer>> listlist = new ArrayList<List<Integer>>();
        List<Integer> list = new ArrayList<Integer>();
        if (null == candidates || 0 == candidates.length) {
            listlist.add(list);
            return listlist;
        }

        Arrays.sort(candidates);
        combinationSum2(candidates, target, 0, list, listlist);
        return listlist;
    }

    private void combinationSum2(int[] candidates, int target, int index,
            List<Integer> list, List<List<Integer>> listlist) {
        if (target < 0) {
            return;
        }

        if (0 == target) {
            listlist.add(new ArrayList<Integer>(list));
            return;
        }

        for (int i = index; i < candidates.length; i++) {
            if (index != i && candidates[i - 1] == candidates[i]) {
                continue;
            }
            list.add(candidates[i]);
            combinationSum2(candidates, target - candidates[i], i + 1, list, listlist);
            list.remove(list.size() - 1);
        }
    }
}
</code></pre>
