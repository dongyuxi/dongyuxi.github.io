---
layout: post
title: LeetCode 090 - Subsets II - 题解/Solution 
categories: 刷题
tags: leetcode java
keywords: leetcode,java,solution,题解,解题报告
tagline: Supporting tagline
---
***<https://leetcode.com/problems/subsets-ii/>***
<pre><code>/**
 * Given a set of distinct integers, S, return all possible subsets.
 * 
 * Note:
 * 
 * Elements in a subset must be in non-descending order. The solution set must
 * not contain duplicate subsets.
 * 
 * For example, If S = [1,2,3], a solution is:
 * 
 * [ [3], [1], [2], [1,2,3], [1,3], [2,3], [1,2], [] ]
 * 
 * @author dongyuxi
 *
 */
public class Solution {
    public List<List<Integer>> subsetsWithDup(int[] num) {
        List<List<Integer>> listlist = new ArrayList<List<Integer>>();
        List<Integer> list = new ArrayList<Integer>();
        if (null == num || 0 == num.length) {
            listlist.add(list);
            return listlist;
        }

        Arrays.sort(num);
        subsets(num, 0, 0, list, listlist);
        return listlist;
    }

    private void subsets(int[] num, int index, int depth,
            List<Integer> list, List<List<Integer>> listlist) {
        if (depth > num.length) {
            return;
        }

        listlist.add(new ArrayList<Integer>(list));
        for (int i = index; i < num.length; i++) {
            list.add(num[i]);
            subsets(num, i + 1, depth + 1, list, listlist);
            list.remove(list.size() - 1);
            while (i < num.length - 1 && num[i] == num[i + 1]) {
                i++;
            }
        }
    }
}
</code></pre>
