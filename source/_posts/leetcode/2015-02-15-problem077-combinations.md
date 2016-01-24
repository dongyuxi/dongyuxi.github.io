---
layout: post
title: LeetCode 077 - Combinations - 题解/Solution 
categories: 刷题
tags: [leetcode,java]
keywords: leetcode,java,solution,题解,解题报告
date: 2015-02-15
permalink: problem077-combinations
---
***<https://leetcode.com/problems/combinations/>***
<!--more-->
```java
/**
 * Given two integers n and k, return all possible combinations of k numbers out
 * of 1 ... n.
 * 
 * For example, If n = 4 and k = 2, a solution is:
 * 
 * [ [2,4], [3,4], [2,3], [1,2], [1,3], [1,4], ]
 * 
 * 
 * @author dongyuxi
 *
 */
public class Solution {
    public List<List<Integer>> combine(int n, int k) {
        List<List<Integer>> listlist = new ArrayList<List<Integer>>();
        List<Integer> list = new ArrayList<Integer>();
        if (n < k) {
            listlist.add(list);
            return listlist;
        }

        combine(n, k, 0, 0, list, listlist);
        return listlist;
    }

    private void combine(int n, int k, int index, int depth,
            List<Integer> list, List<List<Integer>> listlist) {
        if (depth == k) {
            listlist.add(new ArrayList<Integer>(list));
            return;
        }

        for (int i = index + 1; i <= n; i++) {
            list.add(i);
            combine(n, k, i, depth + 1, list, listlist);
            list.remove(list.size() - 1);
        }
    }
}
```