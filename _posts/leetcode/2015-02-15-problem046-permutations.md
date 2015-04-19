---
layout: post
title: LeetCode 046 - Permutations - 题解/Solution 
categories: Leetcode
tags: leetcode java
keywords: leetcode,java,solution,题解,解题报告
tagline: Supporting tagline
---
***<https://leetcode.com/problems/permutations/>***
<pre><code>/**
 * Given a collection of numbers, return all possible permutations.
 * 
 * For example, [1,2,3] have the following permutations: [1,2,3], [1,3,2],
 * [2,1,3], [2,3,1], [3,1,2], and [3,2,1].
 * 
 * @author dongyuxi
 *
 */
public class Solution {
    public List<List<Integer>> permute(int[] num) {
        List<List<Integer>> listlist = new ArrayList<List<Integer>>();
        if (null == num || 0 == num.length) {
            listlist.add(new ArrayList<Integer>());
            return listlist;
        }

        permute(num, 0, listlist);
        return listlist;
    }

    private void permute(int[] num, int index, List<List<Integer>> listlist) {
        if (num.length - 1 == index) {
            List<Integer> list = new ArrayList<Integer>();
            for (int i = 0; i < num.length; i++) {
                list.add(num[i]);
            }
            listlist.add(list);
            return;
        }
        for (int i = index; i < num.length; i++) {
            swap(num, i, index);
            permute(num, index + 1, listlist);
            swap(num, i, index);
        }
    }

    private void swap(int[] num, int i, int j) {
        int temp = num[i];
        num[i] = num[j];
        num[j] = temp;
    }
}
</code></pre>