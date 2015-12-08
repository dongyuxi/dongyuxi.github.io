---
layout: post
title: LeetCode 119 - Pascal's Triangle II - 题解/Solution 
categories: 刷题
tags: leetcode java
keywords: leetcode,java,solution,题解,解题报告
tagline: Supporting tagline
---
***<https://leetcode.com/problems/pascals-triangle-ii/>***
<pre><code>/**
 * Given an index k, return the kth row of the Pascal's triangle.
 * 
 * For example, given k = 3, Return [1,3,3,1].
 * 
 * Note: Could you optimize your algorithm to use only O(k) extra space?
 * 
 * @author dongyuxi
 *
 */
public class Solution {
    public List<Integer> getRow(int rowIndex) {
        List<Integer> list = new ArrayList<Integer>();
        List<Integer> list2 = new ArrayList<Integer>();

        if (rowIndex < 0) {
            return list;
        }

        for (int i = 0; i <= rowIndex; i++) {
            if (i == 0) {
                list2.add(1);
            } else {
                for (int j = 0; j <= i; j++) {
                    if (j == 0 || j == i) {
                        list2.add(1);
                    } else {
                        list2.add(list.get(j - 1) + list.get(j));
                    }
                }
            }

            List<Integer> temp = list;
            list = list2;
            list2 = temp;
            list2.clear();
        }

        return list;
    }
}
</code></pre>
