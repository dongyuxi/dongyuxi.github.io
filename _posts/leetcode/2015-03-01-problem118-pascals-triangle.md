---
layout: post
title: LeetCode 118 - Pascal's Triangle - 题解/Solution 
categories: 刷题
tags: leetcode java
keywords: leetcode,java,solution,题解,解题报告
tagline: Supporting tagline
---
***<https://leetcode.com/problems/pascals-triangle/>***
<pre><code>/**
 * Given numRows, generate the first numRows of Pascal's triangle.
 * For example, given numRows = 5,
 * Return
 * [
 *      [1],
 *     [1,1],
 *    [1,2,1],
 *   [1,3,3,1],
 *  [1,4,6,4,1]
 * 
 * @author dongyuxi
 *
 */
public class Solution {
    public List<List<Integer>> generate(int numRows) {
        if (numRows < 0) {
            return null;
        }

        List<List<Integer>> list = new ArrayList<List<Integer>>();
        for (int i = 0; i < numRows; i++) {
            List<Integer> curList = new ArrayList<Integer>();
            if (0 == i) {
                curList.add(1);
            } else {
                List<Integer> preList = list.get(i - 1);
                for (int j = 0; j <= i; j++) {
                    if (0 == j || j == i) {
                        curList.add(1);
                    } else {
                        curList.add(preList.get(j - 1) + preList.get(j));
                    }
                }
            }
            list.add(curList);
        }
        return list;
    }
}
</code></pre>
